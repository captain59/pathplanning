#include "Extractor.h"
#include "PathPlanner.h"

int main() {
    Mat img = imread("/home/anirban/programming/Clion_Projects/task/Planning/aa.png", CV_LOAD_IMAGE_COLOR);
    if(!img.data) {
        cout<<" Unable to load Image" <<endl;
        return -1;
    }
    Mat original = img.clone();
    point src = ExtractCenter(img, Scalar(0, 0, 129), Scalar(0, 0, 255));
    point dst = ExtractCenter(img, Scalar(0, 128, 0), Scalar(0, 255, 0));
    matrix obstacleMap = ExtractObstacleMap(img.clone());
    PathPlanner obj = PathPlanner(img.rows, img.cols, src, dst, obstacleMap);
    vector<point> path(obj.getPath());
    for(point& p : path)
        circle(img, Point(p.x, p.y), 1, Scalar(255, 0, 0), 1, CV_FILLED);
    cout << "The number of points traversed: " << obj.pointsTraversed << endl;
    namedWindow("Original", CV_WINDOW_NORMAL);
    namedWindow("Path", CV_WINDOW_NORMAL);
    imshow("Original", original);
    imshow("Path", img);
    waitKey(0);
    destroyAllWindows();
    return 0;
}