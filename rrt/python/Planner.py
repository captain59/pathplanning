import sys, math, random
from rrtnode import RRTNode
import numpy as np 

class PathPlannerRRT:
    
    def __init__(self, src, dst, obstaclemap, delta, NUM_NODES=5000):
        self.src = src
        self.dst = dst
        self.obstaclemap = obstaclemap
        self.delta = delta
        self.NUM_NODES = NUM_NODES

    '''
    obstacleMap is valid if 0 otherwise 1 if there is an obstacle
    '''
    def isValid(self, point):
        row, col = point
        ROW, COL = self.obstaclemap.shape
        return 0 <= row < ROW and 0 <= col < COL and self.obstaclemap[row][col] == 0

    def getRandomClearPoint(self):
        ROW, COL = self.obstaclemap.shape
        while True:
            point = int(random.random()*ROW), int(random.random()*COL)
            if self.isValid(point):
                return point
    
    def distance(self, p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


    def step_from_to(self, p1, p2):
        if self.distance(p1, p2) < self.delta:
            return p2
        else:
            theta = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
            return int(p1[0] + self.delta*math.cos(theta)), int(p1[1] + self.delta*math.sin(theta))


    def pointCircleCollision(self, p1, p2, radius):
        dt = self.distance(p1, p2)
        if dt < radius:
            return True
        return False

    def rrtgetpath(self):
        
        nodes = []
        initialPoint = RRTNode(self.src, None)
        goalPoint = RRTNode(self.dst, None)
        nodes.append(initialPoint)
        currentState = 'buildTree'
        count = 0
        path = []
        while True and count < self.NUM_NODES:
            if currentState == 'buildTree':
                count += 1
                searching = True
                while searching:
                    randPoint = self.getRandomClearPoint()
                    parentNode = nodes[0]
                    for p in nodes:
                        if self.distance(p.point, randPoint) <= self.distance(parentNode.point, randPoint):
                            newPoint = self.step_from_to(p.point, randPoint)
                            if self.isValid(newPoint):
                                parentNode = p
                                searching = False

                newPt = self.step_from_to(parentNode.point, randPoint)
                nodes.append(RRTNode(newPt, parentNode))

                if self.pointCircleCollision(newPt, goalPoint.point, self.delta//2):
                    goalPoint.parent = nodes[-1]
                    currentState = 'goalFound'
            elif currentState == 'goalFound':
                currNode = goalPoint.parent
                print "Goal Reached"
                path.append(self.dst)   
                while currNode.parent:
                    path.append(currNode.point)
                    currNode = currNode.parent
                path.append(self.src)
                return path[::-1]

        if count > self.NUM_NODES:
            print(" Nodes OverExceeded")
        raise ValueError("No Path Found")
