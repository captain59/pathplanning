//
// Created by anirban on 1/9/18.
//
#include "point.h"

point::point() = default;
point::point(int x, int y) {
    this->x = x;
    this->y = y;
}

bool checkPoint(point &p1, point &p2) {
    return p1.x==p2.x && p1.y==p2.y;
}
