#!/usr/bin/env python3.10
import sys

def solvebeam(grid,beam):
    beams = [beam]
    visited = {}
    while len(beams):
        nbeams = []
        for p,d in beams:
            y,x = p
            i,j = d
            di = dirs.index(d)
            if not( 0 <= y+i < ymax and 0<= x+j < xmax):
                continue
            y,x = y+i,x+j
            if (y,x) not in visited:
                visited[(y,x)] = set()
            if d in visited[(y,x)]:
                continue
            else:
                visited[(y,x)].add(d)
            c = grid[y][x]
            if c == '|' and di in (1,3):
                c = '.'
            elif c == '-' and di in (0,2):
                c = '.'
            match c:
                case '.':
                    nbeams.append(((y,x),d))
                case '|':
                    nbeams.append(((y,x),dirs[1]))
                    nbeams.append(((y,x),dirs[3]))
                case '-':
                    nbeams.append(((y,x),dirs[0]))
                    nbeams.append(((y,x),dirs[2]))
                case '/':
                    if di in (0,2):
                        d = dirs[(di-1)%4]
                    else:
                        d = dirs[(di+1)%4]
                    nbeams.append(((y,x),d))
                case '\\':
                    if di in (0,2):
                        d = dirs[(di+1)%4]
                    else:
                        d = dirs[(di-1)%4]
                    nbeams.append(((y,x),d))
                case _:
                    print("panic ", y,x,c,d) 
        beams = nbeams
    return len(visited)


dirs = [(0,1),(1,0),(0,-1),(-1,0)]
if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    grid = []
    for line in lines:
        grid.append([c for c in line])
    ymax,xmax = len(grid),len(grid[0])
    print(solvebeam(grid,((0,-1),(0,1))))
    res = []
    for y in range(ymax):
        res.append(solvebeam(grid,((y,-1),(0,1))))
        res.append(solvebeam(grid,((y,xmax),(0,-1))))
    for x in range(xmax):
        res.append(solvebeam(grid,((-1,x),(1,0))))
        res.append(solvebeam(grid,((ymax,x),(-1,0))))
    print(max(res))
