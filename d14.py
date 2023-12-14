#!/usr/bin/env python3.10
import sys

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    grid = []
    for line in lines:
        grid.append(list(line))

    for y in range(1,len(grid)):
        for x,c in enumerate(grid[y]):
            if c == 'O':
                yn=y
                done = False
                while not done:
                    if yn>0 and grid[yn-1][x] == '.':
                        yn -= 1
                    else:
                        done = True
                if yn != y:
                    grid[yn][x] = c
                    grid[y][x] = '.'
    print(sum([r.count('O')*(len(grid)-i) for i,r in enumerate(grid)]))

    grid = []
    for line in lines:
        grid.append(list(line))
    cache ={}
    values={}
    for z in range(1000000000):
        for y in range(1,len(grid)):
            for x,c in enumerate(grid[y]):
                if c == 'O':
                    yn=y
                    done = False
                    while not done:
                        if yn>0 and grid[yn-1][x] == '.':
                            yn -= 1
                        else:
                            done = True
                    if yn != y:
                        grid[yn][x] = c
                        grid[y][x] = '.'
        for y in range(len(grid)):
            for x in range(1,len(grid[y])):
                c = grid[y][x]
                if c == 'O':
                    xn=x
                    done = False
                    while not done:
                        if xn>0 and grid[y][xn-1] == '.':
                            xn -= 1
                        else:
                            done = True
                    if xn != x:
                        grid[y][xn] = c
                        grid[y][x] = '.'
        for y in range(len(grid)-1,-1,-1):
            for x,c in enumerate(grid[y]):
                if c == 'O':
                    yn=y
                    done = False
                    while not done:
                        if yn<len(grid)-1 and grid[yn+1][x] == '.':
                            yn += 1
                        else:
                            done = True
                    if yn != y:
                        grid[yn][x] = c
                        grid[y][x] = '.'
        for y in range(len(grid)):
            for x in range(len(grid[y])-1,-1,-1):
                c = grid[y][x]
                if c == 'O':
                    xn=x
                    done = False
                    while not done:
                        if xn<len(grid[y])-1 and grid[y][xn+1] == '.':
                            xn += 1
                        else:
                            done = True
                    if xn != x:
                        grid[y][xn] = c
                        grid[y][x] = '.'
        key = '_'.join([''.join(r) for r in grid])
        if key in cache:
            print(values[cache[key] + (1000000000-1 - cache[key])% (z-cache[key])])
            break
        else:
            cache[key] = z
            values[z] = sum([r.count('O')*(len(grid)-i) for i,r in enumerate(grid)])
