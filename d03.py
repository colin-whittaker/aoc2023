#!/usr/bin/env python3.10
import sys

def find_starts(grid, x,y):
    neigh = [ (-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1) ]
    starts = set()
    for i,j in neigh:
        a,b = x+i,y+j
        if a<0 or a==xlim or b<0 or b==ylim:
            next
        if grid[b][a].isdigit():
            while a>0 and grid[b][a-1].isdigit():
                a -= 1
            starts.add((a,b) )
    return starts

def start2int(grid, x,y):
    z = x+1
    while z<xlim and grid[y][z].isdigit():
        z +=1
    return int(grid[y][x:z])
         
if __name__ == '__main__':
    grid = list(line.rstrip() for line in sys.stdin)
    #do stuff
    xlim = len(grid[0])
    ylim = len(grid)
    starts = set()
    tot = 0
    tot2 = 0
    for y in range(ylim):
        for x,c in enumerate(grid[y]):
            if c != '.' and not c.isdigit():
                s = find_starts(grid, x,y)
                starts.update(s)
                if c == '*' and len(s) == 2:
                    nums = []
                    for a,b in s:
                        nums.append(start2int(grid,a,b))
                    tot2 += nums[0]*nums[1]
    for x,y in starts:
        tot += start2int(grid,x,y)
    print(tot)
    print(tot2)
