import cv2
import pickle
import cvzone
import numpy as np
import mysql.connector
from datetime import datetime, timedelta

# Video feed
cap = cv2.VideoCapture("ParkVideo.mp4")

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

# Dictionary to track entry times
entry_times = {}

def checkParkingSpace(imgPro):
    spaceCounter = 0
    status = {}
    timestamp = datetime.now()

    for i, pos in enumerate(posList):
        x, y = pos

        imgCrop = imgPro[y : y + height, x : x + width]
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
            status[f"space_{i+1}"] = 1  # 1 means vacant

            # Check if the space was previously occupied
            if i+1 in entry_times:
                # Calculate duration and cost
                entry_time = entry_times.pop(i+1)
                duration = timestamp - entry_time
                hours_parked = duration.total_seconds() / 3600
                parked_time = hours_parked* 1000
                cost = round(parked_time * 100, 2)

                # Record the billing information
                cursor.execute('INSERT INTO Billing (space_id, entry_time, exit_time, cost) VALUES (%s, %s, %s, %s)', 
                            (i+1, entry_time, timestamp, cost))
                conn.commit()
        else:
            color = (0, 0, 255)
            thickness = 2
            status[f"space_{i+1}"] = 0  # 0 means occupied

            # Record the entry time if the space is newly occupied
            if i+1 not in entry_times:
                entry_times[i+1] = timestamp

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(
            img,
            str(count),
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
conn.close()
