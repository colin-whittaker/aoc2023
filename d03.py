#!/usr/bin/env python3.10
import sys

neigh = [ (-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1) ]
if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    grid = []
    for line in lines:
        grid.append(line)
    xlim = len(line)
    ylim = len(grid)
    sym = []
    gearsym = []
    for y in range(ylim):
        for x,c in enumerate(grid[y]):
            if c != '.' and not c.isdigit():
                sym.append((x,y))
                if c == '*':
                    gearsym.append((x,y))
    starts = set()
    for x,y in sym:
        for i,j in neigh:
            a,b = x+i,y+j
            if a<0 or a==xlim or b<0 or b==ylim:
                next
            if grid[b][a].isdigit():
                while a>0 and grid[b][a-1].isdigit():
                    a -= 1
                starts.add((a,b) )
    tot = 0
    for x,y in starts:
        z = x+1
        while z<xlim and grid[y][z].isdigit():
            z +=1
        tot += int(grid[y][x:z])
    print(tot)

    tot = 0
    for x,y in gearsym:
        starts = set()
        for i,j in neigh:
            a,b = x+i,y+j
            if a<0 or a==xlim or b<0 or b==ylim:
                next
            if grid[b][a].isdigit():
                while a>0 and grid[b][a-1].isdigit():
                    a -= 1
                starts.add((a,b) )
        if len(starts) == 2:
            nums = []
            for x,y in starts:
                z = x+1
                while z<xlim and grid[y][z].isdigit():
                    z +=1
                nums.append(int(grid[y][x:z]))
            tot += nums[0]*nums[1]
    print(tot)
 
