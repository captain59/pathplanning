//
// Created by anirban on 1/6/18.
//

#ifndef VISION_EXTRACTOR_H
#define VISION_EXTRACTOR_H

#include "point.h"

point ExtractCenter(Mat img, Scalar lowerRange, Scalar upperRange);

matrix ExtractObstacleMap(Mat img);

#endif //VISION_EXTRACTOR_H
