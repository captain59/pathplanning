import cv2
import numpy as np
import sys
import ExtractCenter
from Planner import PathPlannerAStar

if __name__ == '__main__':
    fileLocation = "../../data/aa.png"
    img = cv2.imread(fileLocation, cv2.IMREAD_COLOR)
    if img is None:
        print "Unable to load image"
        sys.exit(-1)
    # OpenCV uses BGR colour space as default
    imgCopy = img.copy()
    blue, black = np.array([255, 0, 0]), np.array([0, 0, 0])
    lowerRedRange, upperRedRange = np.array([0, 0, 128]), np.array([0, 0, 255])
    lowerGreenRange, upperGreenRange = np.array([0, 128, 0]), np.array([0, 255, 0])
    src = ExtractCenter.extractpoint(img, lowerRedRange, upperRedRange)
    dst = ExtractCenter.extractpoint(img, lowerGreenRange, upperGreenRange)
    obs = ExtractCenter.obtainObstacleMap(img)
    print src, dst, obs.shape
    obj = PathPlannerAStar(src, dst, obs)
    path = obj.astartgetPath()
    for point in path:
        cv2.circle(img, point[::-1], 1, blue, cv2.FILLED)
    cv2.circle(img, src[::-1], 3, black, cv2.FILLED)
    cv2.circle(img, dst[::-1], 3, black, cv2.FILLED)
    cv2.namedWindow('Display Path', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Original Image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Original Image', imgCopy)
    cv2.imshow('Display Path', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
