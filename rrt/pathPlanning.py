import cv2
import numpy as np
import sys
import ExtractCenter

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
    obs = ExtractCenter.obtainObstacleMap(img)
    print src, dst, obs.shape
