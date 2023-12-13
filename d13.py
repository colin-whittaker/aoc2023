#!/usr/bin/env python3.10
import sys
import copy

def find_reflect(grid,old=(-1,-1)):
    ymax = len(grid)
    xmax = len(grid[0])
    # horizontal check
    for y in range(ymax-1):
        y1,y2 = y,y+1
        mirror = True
        while 0 <= y1 and y2 < ymax and mirror:
            for x in range(xmax):
                if grid[y1][x] != grid[y2][x]:
                    mirror = False
            y1,y2 = y1 -1, y2+1
        if mirror and y != old[0] - 1:
            return (y+1,0)
    # vertical check
    for x in range(xmax-1):
        x1,x2 = x,x+1
        mirror = True
        while 0 <= x1 and x2 < xmax and mirror:
            for y in range(ymax):
                if grid[y][x1] != grid[y][x2]:
                    mirror = False
            x1,x2 = x1 -1, x2+1
        if mirror and x != old[1] - 1:
            return (0,x+1)

def find_reflect2(grid):
    old = find_reflect(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] = '.' if grid[y][x] == '#' else '#'
            res = find_reflect(grid,old)
            grid[y][x] = '.' if grid[y][x] == '#' else '#'
            if res:
                return res
     
if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    grids=[]
    grids.append([])
    for line in lines:
        if line == '':
            grids.append([])
        else:
            grids[-1].append(list(line))

    res = []
    for grid in grids:
        res.append(find_reflect(grid))
    print(sum([c+r*100 for r,c in res]))

    res = []
    for grid in grids:
        res.append(find_reflect2(grid))
    print(sum([c+r*100 for r,c in res]))
