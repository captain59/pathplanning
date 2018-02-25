//
// Created by anirban on 1/6/18.
//
#include "PathPlanner.h"

node::node() = default;
node::node(point pnt, point parent, double h, double g, bool visited) {
    this->pt = pnt;
    this->parent = parent;
    this->h = h;
    this->g = g;
    this->visited = visited;
}

PathPlanner::PathPlanner(unsigned int ROW, unsigned int COL, point src, point dst, matrix& obstacleMap) {
    this->src = src;
    this->dst = dst;
    this->obstacleMap = obstacleMap;
    this->ROW = ROW;
    this->COL = COL;
}

bool PathPlanner::isValid(point p) {
    return p.x >= 0 && p.x < COL && p.y >=0 && p.y < ROW && obstacleMap[p.y][p.x];
}

double PathPlanner::heuristic(point p, string& type) {
    if(type.compare("manhattan") == 0)
        return abs(p.x-dst.x)+abs(p.y-dst.y);
    else
        return sqrt(pow(p.x - dst.x, 2) + pow(p.y - dst.y, 2));
}

vector<point> PathPlanner::childrenPoint(point p) {
    vector<point > neighbours = {point(p.x-1, p.y), point(p.x+1, p.y), point(p.x, p.y-1), point(p.x, p.y+1),
                                 point(p.x-1, p.y-1), point(p.x+1, p.y-1), point(p.x+1, p.y+1), point(p.x-1, p.y+1) };
    vector<point > validneighbours;
    for(const point &po : neighbours) {
        if(isValid(po))
            validneighbours.push_back(po);
    }
    return validneighbours;
}

vector<point> PathPlanner::getPath() {
    if(!isValid(src) || !isValid(dst)) {
        throw std::runtime_error("Source or Destination is invalid.");
    }
    vector<vector<node> > grid(ROW, vector<node > (COL));
    point srcParent = point(-1, -1);
    for(int i=0; i< ROW; i++) for(int j=0; j< COL; j++) grid[i][j] = node(point(j, i), srcParent);
    grid[src.y][src.x].parent = srcParent, grid[src.y][src.x].h = 0.0, grid[src.y][src.x].g = 0.0;
    node current(src, srcParent, 0.0, 0.0, false);
    set<node> openSet;
    openSet.insert(current);
    while (!openSet.empty()) {
        current = *(openSet.begin());
        // Traceback the Path
        if( checkPoint(current.pt, dst)) {
            vector<point > path;
            while (!checkPoint(current.parent, srcParent)) {
                path.push_back(current.pt), pointsTraversed ++ ;
                current = grid[current.parent.y][current.parent.x];
            }
            path.push_back(current.pt), pointsTraversed ++;
            reverse(path.begin(), path.end());
            return path;
        }
        grid[current.pt.y][current.pt.x].visited = true;
        openSet.erase(current);
        vector<point > validneighbours = childrenPoint(current.pt);
        for(point ptn : validneighbours) {
            //cout << ptn.y << " " << ptn.x << " " <<grid[ptn.y][ptn.x].visited<< endl;
            if(grid[ptn.y][ptn.x].visited) continue;
            bool preset = false;
            for(auto n: openSet) {
                if(checkPoint(n.pt, ptn)) {
                    preset = true;
                    break;
                }
            }
            if(preset) {
                double nG = grid[current.pt.y][current.pt.x].g + (ptn.x == current.pt.x || ptn.y == current.pt.y)? 1.0 : sqrt(2);
                if(grid[ptn.y][ptn.x].g > nG) {
                    grid[ptn.y][ptn.x].g = nG;
                    grid[ptn.y][ptn.x].parent = current.parent;
                }
            } else {
                // Either manhattan or eucledian
                string distance = "manhattan";
                grid[ptn.y][ptn.x].g = current.g + (ptn.x == current.pt.x || ptn.y == current.pt.y)? 1.0 : sqrt(2);
                grid[ptn.y][ptn.x].h = heuristic(ptn, distance);
                grid[ptn.y][ptn.x].parent = current.pt;
                openSet.insert(node(ptn, current.pt, grid[ptn.y][ptn.x].h, grid[ptn.y][ptn.x].g));
            }
        }
        validneighbours.clear();
    }
    throw runtime_error("No Path Found");
}