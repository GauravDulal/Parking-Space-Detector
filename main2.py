import cv2
import pickle
import cvzone
import numpy as np
import mysql.connector
from datetime import datetime

# Video feed
cap = cv2.VideoCapture("ParkVideo.mp4")

with open("ParkingCoordinates", "rb") as f:
    posList = pickle.load(f)

width, height = 107, 48

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='maroon@&1889',
    database='psds'
)
cursor = conn.cursor()

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
        else:
            color = (0, 0, 255)
            thickness = 2
            status[f"space_{i+1}"] = 0  # 0 means occupied

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

        # Insert status into the database
        cursor.execute('INSERT INTO ParkingStatus (timestamp, space_id, status) VALUES (%s, %s, %s)', 
                       (timestamp, i+1, status[f"space_{i+1}"]))

    conn.commit()

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
