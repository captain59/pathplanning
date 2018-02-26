import cv2
import numpy as np
import sys
import ExtractCenter
from Planner import PathPlannerRRT

if __name__ == '__main__':
    fileLocation = "../data/aa.png"
    img = cv2.imread(fileLocation, cv2.IMREAD_COLOR)
    if img is None:
        print 'Unable to load image'
        sys.exit(-1)
    # OpenCV uses BGR colour space as default
    imgCopy = img.copy()
    blue, black = np.array([255, 0, 0]), np.array([0, 0, 0])
    lowerRedRange, upperRedRange = np.array([0, 0, 128]), np.array([0, 0, 255])
    lowerGreenRange, upperGreenRange = np.array([0, 128, 0]), np.array([0, 255, 0])
    src = ExtractCenter.extractpoint(img, lowerRedRange, upperRedRange)
    dst = ExtractCenter.extractpoint(img, lowerGreenRange, upperGreenRange)
    obstacle = ExtractCenter.obtainObstacleMap(img)
    print src, dst, obstacle.shape
    obj = PathPlannerRRT(src, dst, obstacle, 10, 8000)
    path = obj.rrtgetpath()
    print path[0], path[-1], len(path)
    cv2.circle(img, src[::-1], 3, black, cv2.FILLED)
    cv2.circle(img, dst[::-1], 3, black, cv2.FILLED)
    lastPoint = src
    for point in path:
        cv2.line(img, point[::-1], lastPoint[::-1], blue, 2, cv2.FILLED)
        lastPoint = point
    cv2.namedWindow('Display Path', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Original Image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Original Image', imgCopy)
    cv2.imshow('Display Path', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()