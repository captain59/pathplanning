cmake_minimum_required(VERSION 3.9)
project(vision)
find_package( OpenCV REQUIRED )
set(CMAKE_CXX_STANDARD 17)

add_executable(vision main.cpp PathPlanner.cpp PathPlanner.h Extractor.cpp Extractor.h point.cpp point.h)
include_directories(${OpenCV_INCLUDE_DIRS})
target_link_libraries(vision ${OpenCV_LIBS})