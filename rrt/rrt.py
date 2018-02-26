import numpy as np 
import random, time, sys, math


class Node(object):
	def __init__(self, point, parent):
		super(Node, self).__init__()
		self.point = point
		self.parent = parent
		

def point_circle_collision(p1, p2, radius):
	distance = dist(p1, p2)
	if (distance <= radius):
		return True
	return False

def step_from_to():
	if dist(pi, p2) < delta:
		return p2
	else:
		theta = atan2((p2[1]-p1[1])/(p2[0]-p1[0]))
		return p1[0] + delta*cos(theta), p1[1] + delta*sin(theta)


def dist(p1, p2):
	return sqrt((p1[0]-p2[0])**2 + (p1[1-p2[1]])**2)

def collides(p):
	return 0<= p[0] < YDIM and 0<= p[1] < XDIM and obstacleMap[row][col] == 0

def get_random_clear():
	while True:
		p = random.random()*XDIM, random.random()*YDIM
		noCollision = collides(p)
		if not noCollision:
			return p

XDIM = 600
YDIM = 480
GOAL_RADIUS = 10
delta = 10.0
initialPoint = Node(src, None)
goalPoint = Node(dst, None)

nodes = []
nodes.append(initialPoint)
initPoseSet = True
goalPoseSet = True
rectObs = []
tracebackpoints = []
currentState = 'init'
count, NUMNODES = 0, 5000
while True:

	if currentState == 'init':
		print('Starting Searching for goal')
	elif currentState == 'goalFound':
		currNode = goalNode.parent
		print('Goal Reached')

		while currNode.parent:
			tracebackpoints.append(currNode.point)
			currNode = currNode.parent
	elif currentState == 'buildTree':
		count = count + 1
		print('Performing RRT')
		if count < NUMNODES:
			foundNext = False
			while foundNext == False:
				rand = get_random_clear()
				parentNode = nodes[0]
				for p in nodes:
					if dist(p.point, rand) <= dist(parentNode.point, rand):
						newPoint = step_from_to(p.point, rand)
						if collides(newPoint) == False:
							parentNode = p
							foundNext = True


			newNode = step_from_to(parentNode.point, rand)
			nodes.append(Node(newNode, parentNode))

			if point_circle_collision(newNode, goalPoint.point, GOAL_RADIUS):
				currentState = 'goalFound'
				goalNode = nodes[-1]
		else:
			print('Ran out of nodes')
			return;

