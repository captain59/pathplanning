//
// Created by anirban on 1/6/18.
//

#ifndef VISION_PATHPLANNER_H
#define VISION_PATHPLANNER_H

#include <set>
#include <queue>
#include <system_error>
#include <cmath>
#include <algorithm>
#include "point.h"

class node {
public:
    point pt, parent;
    double h, g;
    bool visited;
    node();
    node(point pnt, point parent, double h = numeric_limits<double>::max(), double g = numeric_limits<double>::max(),
         bool visited = false);
    bool operator < (const node &n) const {
        return g + h < n.g + n.h;
    }
};

class PathPlanner {
public:
    point src, dst;
    matrix obstacleMap;
    unsigned int ROW, COL, pointsTraversed = 0 ;
    PathPlanner(unsigned int ROW, unsigned int COL, point src, point dst, matrix& obstacleMap);
    bool isValid(point p);
    double heuristic(point p, string& type);
    vector<point > childrenPoint(point p);
    vector<point > getPath();
};

#endif //VISION_PATHPLANNER_H
