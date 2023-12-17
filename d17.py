#!/usr/bin/env python3.10
import sys
import heapq

def dirs(d):
    ds = [(0,1),(1,0),(0,-1),(-1,0)]
    if d not in ds:
        return ds
    d = ds.index(d)
    return  [ds[(d-1)%4],ds[(d+1)%4]]

def solvegrid(grid,mind,maxd):
    end = (len(grid)-1,len(grid[0])-1)
    costs = [(0,(0,0),(1,1))]
    visit = {}

    while costs:
        score,npos,d = heapq.heappop(costs)
        if npos == end:
            return score
        y,x = npos
        for i,j in dirs(d):
            si = 0
            for dist in range(1,maxd+1):
                a,b = y+i*dist,x+j*dist
                if 0<=a<ymax and 0<=b<xmax:
                    si += grid[a][b]
                    if dist < mind:
                        continue
                    if ((a,b),(i,j)) not in visit or score+si < visit[((a,b),(i,j))]:
                        heapq.heappush(costs,(score+si,(a,b),(i,j)))
                        visit[((a,b),(i,j))] = score +si

if __name__ == '__main__':
    grid = []
    for line in list(line.rstrip() for line in sys.stdin):
        grid.append([int(c) for c in line])
    ymax,xmax = len(grid),len(grid[0])  
    print(solvegrid(grid,1,3))
    print(solvegrid(grid,4,10))
