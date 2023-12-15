#!/usr/bin/env python3.10
import sys

def h(s):
    cv = 0
    for c in s:
        cv += ord(c)
        cv *= 17
        cv %= 256
    return cv

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    tot = 0
    for line in lines[0].split(','):
        tot += h(line)
    print(tot)
    boxes = [ list() for _ in range(256)]

    for line in lines[0].split(','):
        if '=' in line:
            l,op,fl = line[:-2],line[-2],line[-1]
        else:
            l,op,fl = line[:-1],line[-1],-1
        b = h(l)
        if op == '=':
            found = False
            for i in range(len(boxes[b])):
                if boxes[b][i][0] == l:
                    boxes[b][i] = (l,fl)
                    found = True
                    break
            if not found:
                boxes[b].append((l,fl))
        if op == '-':
            if len(boxes[b]) > 0:
                for i in range(len(boxes[b])):
                    if boxes[b][i][0] == l:
                        boxes[b].remove(boxes[b][i])
                        break
    tot = 0
    for j,b in enumerate(boxes):
        for i,v in enumerate(b):
            tot += (j+1) * (i+1) * int(v[1])
    print(tot)
