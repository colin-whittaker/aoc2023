#!/usr/bin/env python3.10
import sys

def freefall(bricks):
    num = 0
    res = []
    landed = set()
    for b in bricks:
        moved = False
        while True:
            nb = [ [x,y,z-1] for x,y,z in b ]
            if any((p[2] == 0 or (tuple(p) in landed)) for p in nb):
                break
            else:
                b = nb
                moved = True
        for p in b:
            landed.add(tuple(p))
        res.append(b)
        num += 1 if moved else 0
    return res,num

if __name__ == '__main__':
    bricks = []
    for line in sys.stdin:
        c1,c2 = line.split('~')
        p = [[int(x) for x in c1.split(',')],[int(x) for x in c2.split(',')]]
        for i in range(3): 
            if p[0][i] != p[1][i]:
                for j in range(min(p[0][i],p[1][i])+1,max(p[0][i],p[1][i])):
                    p.append(p[0][:i]+[j]+p[0][i+1:])
        bricks.append(p)
    bricks = sorted(bricks, key=lambda b: min(p[2] for p in b)) 

    bricks, total = freefall(bricks)

    res1,res2 = 0,0
    for i in range(len(bricks)):
        nb = bricks[:i]+bricks[i+1:]
        nb, total = freefall(nb)
        res1 += 1 if total == 0 else 0
        res2 += total
    print(res1)
    print(res2)
