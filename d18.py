#!/usr/bin/env python3.10
import sys

dirs = { 'R':(0,1), 'L':(0,-1), 'U':(-1,0), 'D':(1,0),
         '0':(0,1), '2':(0,-1), '3':(-1,0), '1':(1,0)}

def solve(steps):
    y,x = 0,0
    p,a = 0,0
    for d,l in steps:
        i,j = dirs[d][0]*l,dirs[d][1]*l
        y,x = y+i,x+j
        p += l
        a += x*i
    return a+p//2+1

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    steps = []
    steps2 = []
    for line in lines:
        d,l,c = line.split()
        steps.append((d,int(l)))
        d,l = c[-2],c[-7:-2]
        steps2.append((d,int(l,16)))

    print(solve(steps))
    print(solve(steps2))
