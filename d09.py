#!/usr/bin/env python3.10
import sys

def solve(d,r=False):
    n = [ x[1]-x[0] for x in zip(d,d[1:]) ]
    if set(n) == {0}:
        return 0
    n2 = solve(n,r)
    return n[-1] + n2 if not r else n[0] - n2

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    tot = 0 
    res = 0
    for line in lines:
        data = [ int(x) for x in line.split() ]
        tot += data[-1] + solve(data)
        res += data[0] - solve(data,True)
    print(tot)
    print(res)
