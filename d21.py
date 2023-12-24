#!/usr/bin/env python3.10
import sys

def newpos2(grid,p):
    y,x = p
    res = []
    ymax,xmax = len(grid),len(grid[0])
    for i,j in ((-1,0),(1,0),(0,1),(0,-1)):
        if (y+i,x+j) not in pos and grid[(y+i)%ymax][(x+j)%xmax] =='.':
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
    pos = {start:0}
    t = 26501365
    a,b = 1,0
    xmax=len(grid[0])
    res =[]
    while len(res) < 3:
        np = []
        for p in pos:
            if pos[p] == (a+1)%2:
                np.extend(newpos2(grid,p))
        for p in np:
            if p not in pos:
                pos[p] = a%2
        if a%xmax == t%xmax:
            b = sum( 1 if pos[p] == a%2 else 0 for p in pos)
            res.append(b)
        if a == 64:
            print(sum(1 if pos[p] == a%2 else 0 for p in pos))
        a+=1
    a0,a1,a2 = res
    b1,b2 = a1-a0,a2-a1
    x = t//xmax
    print(a0+b1*x+(x*(x-1)//2)*(b2-b1))
