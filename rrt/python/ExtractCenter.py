import cv2
import numpy as np


def extractpoint(img, lowerRange, upperRange):
    mask = cv2.inRange(img, lowerRange, upperRange)
    # Find the contours in the image
    _, contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    M = cv2.moments(contours[0])
    cx, cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    return cy, cx


def obtainObstacleMap(img):
    w, h, _ = img.shape
    white = (255, 255, 255)
    image = np.zeros((w, h), dtype=np.uint8)
    image[np.where((img == white).all(axis=2))] = 255
    retImg = image.copy()
    for i in range(w-3):
        for j in range(h-3):
            if image[i][j] == 255:
                retImg[i][j-1], retImg[i][j-2], retImg[i][j-3] = 255, 255, 255
                retImg[i][j + 1], retImg[i][j + 2], retImg[i][j + 3] = 255, 255, 255
    return retImg
