import cv2
import pickle
import cvzone
import numpy as np

width, height = 107, 48
posList = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)


while True:
    img = cv2.imread('ParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (0, 0, 255), 2)
    cv2.imshow("test", img)
    cv2.setMouseCallback("test", mouseClick)
    key = cv2.waitKey(10)
    if key == ord("q"):
        break

