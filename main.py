import cv2
import pickle
import cvzone
import numpy as np

# Video feed
cap = cv2.VideoCapture("ParkVideo.mp4")

with open("ParkingCoordinates", "rb") as f:
    posList = pickle.load(f)

width, height = 107, 48


def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y : y + height, x : x + width]
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

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
    # Check if we have reached the end of the video
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # Read a frame from the video
    success, img = cap.read()

    # Convert the frame to grayscale and apply image processing
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(
        imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16
    )
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    # Check parking space occupancy
    checkParkingSpace(imgDilate)

    # Display the processed frame with parking space information
    cv2.imshow("Image", img)

    # Check for key press to exit
    key = cv2.waitKey(10)
    if key == ord("q"):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
