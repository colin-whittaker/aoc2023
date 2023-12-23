#!/usr/bin/env python3.10
import sys
from collections import deque

def printgrid(grid):
    for line in grid:
        print(''.join(line))

directions = ((-1,0),(0,1),(1,0),(0,-1))
slopes = '^>v<'

def solve(nodes,icy):
    paths = {}
    for y,x in nodes:
        paths[(y,x)] = []
        queue = deque([(y,x,0)])
        visited = set()
        while queue:
            a,b,d = queue.popleft()
            if (a,b) in visited:
                continue
            visited.add((a,b))
            if (a,b) in nodes and (a,b) != (y,x):
                paths[(y,x)].append(((a,b),d))
                continue
            for i,j in directions:
                if 0<=a+i<ymax and grid[a+i][b+j] != '#':
                    if icy and grid[a][b] in slopes and slopes.index(grid[a][b]) != directions.index((i,j)):
                        continue
                    queue.append((a+i,b+j,d+1))
    visited.clear()
    return pathfind(start,paths,visited)

def pathfind(node,paths,visited,l=0):
    visited.add(node)
    res = [0]
    if node == end:
        res.append(l)
    for nn,c in paths[node]:
        if nn not in visited:
            res.append(pathfind(nn,paths,visited,l+c))
    visited.remove(node)
    return(max(res))

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    grid =[]
    for line in lines:
        grid.append([c for c in line])
    ymax,xmax = len(grid),len(grid[0])
    start = (0,grid[0].index('.'))
    end = (ymax-1,grid[-1].index('.'))
    nodes = set([start,end])
    for y in range(1,ymax-1): # taking advantage of the border
        for x in range(1,xmax-1):
            if grid[y][x] == '#':
                continue
            n = 0
            for i,j in directions:
                n += 1 if grid[y+i][x+j] != '#' else 0
            if n > 2:
                nodes.add((y,x))
    print(solve(nodes,True))
    print(solve(nodes,False))
