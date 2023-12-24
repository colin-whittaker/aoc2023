#!/usr/bin/env python3.10
import sys
import itertools
import z3

def test_collide(a,b):
    ax1,ay1,az1,vx1,vy1,vz1 = hail[a]
    ax2,ay2 = ax1+vx1,ay1+vy1
    bx1,by1,bz1,vx2,vy2,vz2 = hail[b]
    bx2,by2 = bx1+vx2,by1+vy2

    den = ((ax1-ax2)*(by1-by2)-(ay1-ay2)*(bx1-bx2))
    if den == 0:
        return False
    x = ( (ax1*ay2 - ay1*ax2)*(bx1-bx2) - (ax1-ax2)*(bx1*by2-by1*bx2)) / den
    y = ( (ax1*ay2 - ay1*ax2)*(by1-by2) - (ay1-ay2)*(bx1*by2-by1*bx2)) / den
    #bot,top = 7,27
    bot,top = 200000000000000,400000000000000
    if bot <= x <=top and bot <= y <= top and (x>ax1)==(ax2>ax1) and (x>bx1)==(bx2>bx1):
        return True
    return False
    
if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    hail = []
    for line in lines:
        hail.append( [ int(x) for x in line.replace(' @',',').split(', ')] )
    n = len(hail)
    count = 0
    for a,b in itertools.combinations(range(n),2):
        count += 1 if test_collide(a,b) else 0
    print(count)
    
    x,y,z,vx,vy,vz = [z3.Int(c) for c in 'x y z vx vy vz'.split()]
    solve = z3.Solver()
    for i in range(n):
        time = z3.Int(f'T{i}') 
        solve.add(x + time*vx - hail[i][0] - time*hail[i][3] == 0)
        solve.add(y + time*vy - hail[i][1] - time*hail[i][4] == 0)
        solve.add(z + time*vz - hail[i][2] - time*hail[i][5] == 0)
    solve.check()
    model = solve.model()
    print(model.eval(x+y+z))
