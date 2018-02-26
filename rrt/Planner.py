import sys, math

class PathPlannerRRT:
    
    def __init__(self, src, dst, obstaclemap):
        self.src = src
        self.dst = dst
        self.obstaclemap = obstaclemap

    '''
    obstacleMap is valid if 0 otherwise 1 if there is an obstacle
    '''
    def isValid(self, point):
        row, col = point
        ROW, COL = self.obstaclemap.shape
        return 0 <= row < ROW and 0 <= col < COL and self.obstaclemap[row][col] == 0

    
