#!/usr/bin/env python3.10
import sys

def newpos(grid,p):
    y,x = p
    res = []
    ymax,xmax = len(grid)-1,len(grid[0])-1
    for i,j in ((-1,0),(1,0),(0,1),(0,-1)):
        if 0<=y+i<=ymax and 0<=x+j<=xmax:
            if grid[y+i][x+j] =='.':
                res.append((y+i,x+j))
    return res

def newpos2(grid,p):
    y,x = p
    res = []
    ymax,xmax = len(grid),len(grid[0])
    for i,j in ((-1,0),(1,0),(0,1),(0,-1)):
        if grid[(y+i)%ymax][(x+j)%xmax] =='.':
            res.append((y+i,x+j))
    return res


if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    grid = []
    for line in lines:
        grid.append([c for c in line])
        if 'S' in line:
            start = (len(grid)-1,line.index('S'))
            grid[start[0]][start[1]] = '.'
    pos = [start]
    for _ in range(64):
        np = []
        for p in pos:
            np += newpos(grid,p)
        pos = set(np)
    print(len(pos))
    pos = [start]
    t = 26501365
    a,b = 1,0
    xmax=len(grid[0])
    res =[]
    while len(res) < 3:
        np = []
        for p in pos:
            np += newpos2(grid,p)
        pos = set(np)
        if a%xmax == t%xmax:
            res.append(len(pos))
            b = len(pos)
        a+=1
    a0,a1,a2 = res
    b1,b2 = a1-a0,a2-a1
    x = t//xmax
    print(a0+b1*x+(x*(x-1)//2)*(b2-b1))
