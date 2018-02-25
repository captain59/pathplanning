//
// Created by anirban on 1/9/18.
//

#ifndef VISION_POINT_H
#define VISION_POINT_H

#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <vector>
#include <iostream>
using namespace std;
using namespace cv;

typedef vector<vector<bool > > matrix;

class point {
public:
    int x, y;
    point();
    point(int x, int y);
    bool operator < (const point &right) const {
        return x < right.x;
    }
};

bool checkPoint(point& p1, point& p2);
#endif //VISION_POINT_H
