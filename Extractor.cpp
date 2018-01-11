//
// Created by anirban on 1/6/18.
//

#include "Extractor.h"

point ExtractCenter(Mat img, Scalar lowerRange, Scalar upperRange) {
    Mat mask(img.rows, img.cols, CV_8UC1, Scalar(0));
    inRange(img, lowerRange, upperRange, img);
    threshold(img, mask, 220, 255, THRESH_BINARY_INV);
    vector<vector<Point > > contours;
    vector<Vec4i > heirarchy;
    findContours(img, contours,heirarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0) );
    Moments m = moments(contours[0], false);
    point center((int)(m.m10/m.m00), (int)(m.m01/m.m00));
    return center;
}

matrix ExtractObstacleMap(Mat img) {
    unsigned int value = 255;
    matrix obs((unsigned int) (img.rows), vector<bool>((unsigned int) (img.cols)));
    for (int i = 3; i < img.rows-3; i++) {
        for (int j = 2; j < img.cols - 2; j++) {
            if(img.at<Vec3b>(i + 3, j)[0] == value && img.at<Vec3b>(i + 3, j)[1] == value && img.at<Vec3b>(i + 3, j)[2] == value) {
                obs[i][j] = false, obs[i+1][j] = false, obs[i+2][j] = false, obs[i+2][j] = false ;
            }
            else if(img.at<Vec3b>(i - 3, j)[0] == value && img.at<Vec3b>(i - 3, j)[1] == value && img.at<Vec3b>(i - 3, j)[2] == value) {
                obs[i][j] = false, obs[i-1][j] = false, obs[i-2][j] = false, obs[i-3][j] = false ;
            } else
                obs[i][j] = true;
        }
    }
    return obs;
}