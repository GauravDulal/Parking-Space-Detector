import cv2
import pickle
import cvzone
import numpy as np
import mysql.connector
from datetime import datetime

# Video feed
cap = cv2.VideoCapture("ParkVideo.mp4")

# Dictionary to track entry times
entry_times = {}

with open("ParkingCoordinates", "rb") as f:
    posList = pickle.load(f)

width, height = 107, 48

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='psds'
)
cursor = conn.cursor()

# Initialize previous status dictionary
previous_status = {}

def checkParkingSpace(imgPro):
    global previous_status
    spaceCounter = 0
    status = {}
    timestamp = datetime.now()

    for i, pos in enumerate(posList):
        x, y = pos

        imgCrop = imgPro[y : y + height, x : x + width]
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 255, 0)  # green
            thickness = 5
            spaceCounter += 1
            status[f"space_{i+1}"] = True  # True means vacant
            if i+1 in entry_times:
                entry_time = entry_times.pop(i+1)
                duration = timestamp - entry_time
                hours_parked = duration.total_seconds() / 3600
                cost = round(hours_parked * 100, 2)
        else:
            color = (0, 0, 255)  # red
            thickness = 2
            status[f"space_{i+1}"] = False  # False means occupied
            if i+1 not in entry_times:
                entry_times[i+1] = timestamp

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(
            img,
            str(i+1),
            (x, y + height - 3),
            scale=1,
            thickness=2,
            offset=0,
            colorR=color,
        )

    cvzone.putTextRect(
        img,
        f"Free: {spaceCounter}/{len(posList)}",
        (100, 50),
        scale=3,
        thickness=5,
        offset=20,
        colorR=(0, 200, 0),
    )

    # Compare current status with previous status
    for key in status:
        if key in previous_status:
            key_value = key.find('_')
            result = key[key_value + 1:]

            if previous_status[key] == True and status[key] == False:
                if int(result) in entry_times:
                    entry_time = entry_times.pop(int(result))
                    try:
                        cursor.execute(
                            'INSERT INTO log (space_id, log_time, entry_time, exit_time, cost, status, payment_status) VALUES (%s,%s,%s,%s,%s, %s, %s)', 
                            (result, timestamp, entry_time, timestamp, 0, 'Entry', 'Unpaid')
                        )
                        conn.commit()
                        print(f"{key} is logged as Entry")
                    except Exception as e:
                        print(f"Failed to log entry for space {key}: {e}")

            elif previous_status[key] == False and status[key] == True:
                if int(result) in entry_times:
                    entry_time = entry_times.pop(int(result))
                    duration = timestamp - entry_time
                    hours_parked = duration.total_seconds() / 3600
                    cost = round(hours_parked * 500, 2)

                try:
                    cursor.execute(
                        'INSERT INTO log (space_id, log_time, entry_time, exit_time, cost, status, payment_status) VALUES (%s,%s,%s,%s,%s, %s, %s)', 
                        (result, timestamp, entry_time, timestamp, cost, 'Exit', 'Unpaid')
                    )
                    conn.commit()
                    log_id = cursor.lastrowid
                    print(f"{key} is logged as Exit with cost {cost}")
                except Exception as e:
                    print(f"Failed to log exit for space {key}: {e}")
                    
                try:
                    cursor.execute('SELECT * FROM payment WHERE space_id = %s AND payment_status = "Paid"', (result,))
                    payment_record = cursor.fetchone()
                    cursor.fetchall()  # Ensure all results are fetched to avoid unread result error

                    if payment_record:
                        try:
                            cursor.execute(
                                'UPDATE payment SET entry_time = %s, exit_time = %s, cost = %s WHERE space_id = %s AND payment_status = "Unpaid"',
                                (entry_time, timestamp, cost, result)
                            )
                            conn.commit()
                            print(f"Updated payment for space {key} with cost {cost}")
                        except Exception as e:
                            print(f"Failed to update payment for space {key}: {e}")
                    else:
                        if cost > 0:
                            try:
                                cursor.execute(
                                    'INSERT INTO payment (space_id, entry_time, exit_time, cost, payment_status,log_id) VALUES (%s,%s,%s,%s,%s,%s)', 
                                    (result, entry_time, timestamp, cost, 'Unpaid', log_id)
                                )
                                conn.commit()
                                print(f"{key} is inserted into payment with cost {cost}")
                            except Exception as e:
                                print(f"Failed to insert into payment for space {key}: {e}")   
                except Exception as e:
                    print(f"Failed to retrieve payment record for space {key}: {e}")

    previous_status = status.copy()

    with open('parking_status.pkl', 'wb') as file:
        pickle.dump(status, file)


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(
        imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16
    )
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)

    cv2.imshow("Image", img)

    key = cv2.waitKey(10)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
