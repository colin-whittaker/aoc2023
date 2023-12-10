#!/usr/bin/env python3.10
import sys
import heapq

def printgrid(grid,xm,ym):
    for y in range(0,ym):
        print(''.join([str(grid[(x,y)]) if (x,y) in grid else '.' for x in range(0,xm)]) )

def directions(c):
    match c:
        case '|': 
            return [(0,-1),(0,1)]
        case '-': 
            return [(-1,0),(1,0)]
        case 'L': 
            return [(0,-1),(1,0)]
        case 'J': 
            return [(0,-1),(-1,0)]
        case '7': 
            return [(-1,0),(0,1)]
        case 'F': 
            return [(1,0),(0,1)]
        case '.': 
            return []
    print("panic: ",c)

def solve_grid(start,grid,xmax,ymax):
    costs = [(0,start)]
    visit = {}
    visit[start] = 0 
    while True:
        if len(costs) == 0:
            return visit
        score, npos = heapq.heappop(costs)
        x,y = npos
        for i,j in directions(grid[(x,y)]):
            a,b = x+i,y+j
            if 0 <= a < xmax and 0 <= b < ymax:
                if (a,b) not in visit or score+1 < visit[(a,b)]:
                    heapq.heappush(costs,(score+1,(a,b)))
                    visit[(a,b)] = score + 1 

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    ymax = 0
    grid = {}
    for line in lines:
        for x,c in enumerate(line):
            grid[(x,ymax)] = c 
            if c == 'S':
                start = (x,ymax)
        ymax += 1
    xmax = len(line)
    sx,sy = start
    n = []
    for a,b in [ (sx+c,sy+d) for c,d in [(-1,0),(1,0),(0,-1),(0,1)]]:
        if (a,b) in grid: 
            for x,y in [ (a+i,b+j) for i,j in directions(grid[(a,b)]) ]:
                if (x,y) == start:
                    n.append((a-x,b-y))
    for c in '|-LJ7F':
        if n == directions(c):
            grid[start] = c
            break
    if grid[start] == 'S':
            print('Error: ',n)
            sys.exit()
 
    solve = solve_grid(start,grid,xmax,ymax)
    print(max(solve.values()))
    ng = {}
    for p in grid:
        ng[p] = grid[p] if p in solve else '.'
    for y in range(ymax):
        i = False
        for x in range(xmax):
            if ng[(x,y)] in '|JL': 
                i = not i
            elif ng[(x,y)] == '.' and not i:
                    ng[(x,y)] = 0
    print(sum([1 if c == '.' else 0 for c in ng.values()]))
