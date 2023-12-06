#!/usr/bin/env python3.10
import sys
import math

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    times = [ int(x) for x in lines[0].split(':')[1].strip().split() ]
    dist  = [ int(x) for x in lines[1].split(':')[1].strip().split() ]
    print(times,dist)
    ways = []
    for i,t in enumerate(times):
        d = dist[i]
        count = 0
        for z in range(t+1):
            if (z * (t-z)) > d:
                count += 1
        ways.append(count)

    print(ways)
    print(math.prod(ways))

    t = int( ''.join(lines[0].split(':')[1].strip().split()) )
    d = int( ''.join(lines[1].split(':')[1].strip().split()) )
    print(t,d)
    count = 0
    for z in range(t+1):
        if (z * (t-z)) > d:
            count += 1
    print(count)
