#!/usr/bin/env python3.10
import sys

def tilt_grid(grid,dirs=((-1,0),(0,-1),(1,0),(0,1))):
    for i,j in dirs:
        yr,yl,yu = list(range(len(grid))),-1,len(grid)
        xr,xl,xu = list(range(len(grid[0]))),-1,len(grid[0])
        if i == -1:
            yr,yl,yu = list(range(1,len(grid))),0,len(grid)
        elif i == 1:
            yr,yl,yu = list(range(len(grid)-1,-1,-1)),-1,len(grid)-1
        if j == -1:
            xr,xl,xu = list(range(1,len(grid[0]))),0,len(grid[0])
        elif j == 1:
            xr,xl,xu = list(range(len(grid[0])-1,-1,-1)),-1,len(grid[0])-1
        for y in yr:
            for x in xr:
                if grid[y][x] == 'O':
                    yn,xn=y,x
                    done = False
                    while not done:
                        if yl<yn<yu and xl<xn<xu and grid[yn+i][xn+j] == '.':
                            yn,xn = yn+i,xn+j
                        else:
                            done = True
                    if yn != y or xn != x:
                        grid[yn][xn] = grid[y][x]
                        grid[y][x] = '.'
    return grid

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    grid = []
    for line in lines:
        grid.append(list(line))
    grid2 = tilt_grid(grid,[(-1,0)])
    print(sum([r.count('O')*(len(grid)-i) for i,r in enumerate(grid2)]))

    cache ={}
    values={}
    for z in range(1000000000):
        grid = tilt_grid(grid)
        key = '_'.join([''.join(r) for r in grid])
        if key in cache:
            print(values[cache[key] + (1000000000-1 - cache[key])% (z-cache[key])])
            sys.exit()
        else:
            cache[key] = z
            values[z] = sum([r.count('O')*(len(grid)-a) for a,r in enumerate(grid)])
