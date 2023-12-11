#!/usr/bin/env python3.10
import sys
import itertools
import heapq

def distance(start,end,xgap,ygap,scale):
    x,y = 0,0
    for i in xgap:
        if min(start[1],end[1]) <= i < max(start[1],end[1]):
            x += 1
    for i in ygap:
        if min(start[0],end[0]) <= i < max(start[0],end[0]):
            y += 1
    return abs(start[1]-end[1])+x*scale+abs(start[0]-end[0])+y*scale

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    grid = []
    ygap = []
    for line in lines:
        grid.append([c for c in line])
        if not line.count('#'):
            ygap.append(len(grid)-1)
    xgap = []
    for i in range(len(grid[0])):
        ins = True
        for j in range(len(grid)):
            if grid[j][i] == '#':
                ins = False
                break
        if ins:
            xgap.append(i)
    pts = []
    for j in range(len(grid)):
        for i,v in enumerate(grid[j]):
            if v == '#':
                pts.append((j,i))
    pairs = list(itertools.combinations(pts,2))
    res = []
    for start,end in pairs:
        res.append(distance(start,end,xgap,ygap,1))
    print(sum(res))
    res = []
    for start,end in pairs:
        res.append(distance(start,end,xgap,ygap,999999))
    print(sum(res))
