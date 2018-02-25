import sys, math
from astarnode import AstarNode


class PathPlannerAStar:

    def __init__(self, src, dst, obstaclemap):
        self.src = src
        self.dst = dst
        self.obstacleMap = obstaclemap

    def heuristic(self, a, method="manhattan"):
        x1, y1 = a
        x2, y2 = self.dst
        return abs(x1-x2)+abs(y1-y2) if method == "manhattan" else math.sqrt((x1-x2)**2 + (y1-y2)**2)

    def isValid(self, point):
        row, col = point
        ROW, COL = self.obstacleMap.shape
        return 0 <= row < ROW and 0 <= col < COL and self.obstacleMap[row][col] == 0

    def children(self, point):
        x, y = point
        neighbours = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]#, (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]
        validNeighbours = []
        for val in neighbours:
            if self.isValid(val):
                validNeighbours.append(val)
        return validNeighbours

    def astartgetPath(self):
        if not self.isValid(self.src) or not self.isValid(self.dst):
            sys.exit(-1)
        r, c = self.obstacleMap.shape
        srcparent = (-1, -1)
        grid = [[AstarNode((i, j), srcparent, sys.maxint, sys.maxint, False) for j in range(c)] for i in range(r)]
        openset = set()
        grid[self.src[0]][self.src[1]].g, grid[self.src[0]][self.src[1]].h = 0, 0

        current = AstarNode(self.src, srcparent, 0, 0, False)
        openset.add(current)
        # Matrix to check whether element present in openset
        opensetpresent = [[False for _ in range(c)] for _ in range(r)]

        while openset:
            current = min(openset, key=lambda x: x.g + x.h)
            c_i, c_j = current.point
            if current.point == self.dst:
                path = []
                while current.parent != srcparent:
                    path.append(current.point)
                    i, j = current.parent
                    current = grid[i][j]
                path.append(current.point)

                return path[::-1]

            grid[c_i][c_j].visited = True
            openset.remove(current)
            opensetpresent[c_i][c_j] = False

            for pt in self.children(current.point):
                i, j = pt
                if grid[i][j].visited:
                    continue
                # Check if present in opensetpresent
                if opensetpresent[i][j]:
                    weight = 1 #if pt[0] == current.point[0] or pt[1] == current.point[1] else math.sqrt(2)
                    newG = grid[c_i][c_j].g + weight  # move cost
                    if newG < grid[i][j].g:
                        grid[i][j].g = newG
                        grid[i][j].parent = current.point
                else:
                    weight = 1 # if pt[0] == current.point[0] or pt[1] == current.point[1] else math.sqrt(2)
                    grid[i][j].g = current.g + weight
                    grid[i][j].h = self.heuristic(pt)
                    grid[i][j].parent = current.point
                    openset.add(AstarNode(pt, current.point, grid[i][j].h, grid[i][j].g, False))
                    opensetpresent[i][j] = True
        raise ValueError("No Path Found")
