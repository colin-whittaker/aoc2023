#!/usr/bin/env python3.10
import sys
import math
from copy import deepcopy

def process(part,r):
    if r == 'A':
        accept.append(part)
        return
    elif r == 'R':
        return
    rule = rules[r]

    for x in rule:
        if '*' in x:
            process(part,x[0])
            return
        t,c,o,v = x[0],'xmas'.index(x[1]),x[2],int(x[3])
        if o =='<':
            if part[c] < v:
                process(part,t)
                return
        elif o == '>':
            if part[c] > v:
                process(part,t)
                return

def process2(part,r):
    if r == 'A':
        accept.append(tuple(part))
        return
    elif r == 'R':
        return
    rule = rules[r]

    for x in rule:
        if '*' in x:
            process2(part,x[0])
            return
        t,c,o,v = x[0],'xmas'.index(x[1]),x[2],int(x[3])
        s,e = part[c]
        if o =='<':
            if e < v:
                process2(part,t)
                return
            elif s<v<=e:
                p1 = [ p for p in part ]
                p1[c] = (s,v-1)
                part[c] = (v,e)
                process2(p1,t)
        elif o == '>':
            if s > v:
                process2(part,t)
                return
            elif s<=v<e:
                p2 = [ p for p in part ]
                part[c] = (s,v)
                p2[c] = (v+1,e)
                process2(p2,t)

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    mode = 'R'
    rules = {}
    parts = []
    for line in lines:
        if line == '':
            mode = 'P'
            continue
        if mode == 'R':
            label = line[:line.index('{')]
            rules[label] = []
            for r in line[line.index('{')+1:-1].split(','):
                if ':' in r:
                    d,r = r.split(':')
                    rules[label].append((r,d[0],d[1],d[2:]))
                else:
                    rules[label].append((r,'*','*','*'))
        elif mode =='P':
            parts.append(tuple([int(x[2:]) for x in line[1:-1].split(',')]))

    accept = []
    for part in parts:
        process(part,'in')
    print(sum([sum(x) for x in accept]))
    accept = []
    process2([(1,4000),(1,4000),(1,4000),(1,4000)],'in')
    print(sum([math.prod([y[1]+1-y[0] for y in x]) for x in accept]))
