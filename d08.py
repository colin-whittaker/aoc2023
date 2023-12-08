#!/usr/bin/env python3.10
import sys
import math

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    ins = lines.pop(0)
    m = {}
    pos = []
    for line in lines:
        if line:
            node,step = line.split(' = ')
            m[node] = tuple(step[1:-1].split(', '))
            if node[2] == 'A':
                pos.append(node)
    count = 0
    cur = 'AAA'
    while True:
        s = ins[count%len(ins)]
        n = 0 if s == 'L' else 1
        cur = m[cur][n]
        count += 1
        if cur == 'ZZZ':
            break
    print(count)
    counts = []
    for cur in pos:
        done = False
        count=0
        while not done:
            n = 0 if ins[count%len(ins)] == 'L' else 1
            cur = m[cur][n]
            if cur[2] == 'Z':
                    done = True
            count += 1
        counts.append(count)
    print(math.lcm(*counts))
