import sys


class AstarNode:

    def __init__(self, point, parent=(-1, -1), h=sys.maxint, g=sys.maxint, visited=False):
        self.point = point
        self.parent = parent
        self.h = h
        self.g = g
        self.visited = visited
