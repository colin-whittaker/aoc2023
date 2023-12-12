#!/usr/bin/env python3.10
import sys
import functools

@functools.lru_cache(maxsize=None)
def check_strings(s,k):
    res = 0
    key = k
    l = len(s)
    ln = k[-1]
    if sum(k) > l:
        return 0
    if len(k) == 1:
        for pos in range(0,l-ln+1):
            if '#' in s[0:pos]:
                break
            if '.' in s[pos:pos+ln] or '#' in s[pos+ln:]:
                continue
            res += 1
        return res
    for pos in range(l-ln,0,-1):
        if '#' in s[pos+ln:]:
            break
        if '.' not in s[pos:pos+ln]:
            if s[pos-1] == '#':
                continue
            res += check_strings(s[:pos-1],k[:max(0,len(k)-1)])
    return res

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    data = []
    for line in lines:
        s,k = line.split()
        data.append((s,tuple([ int(i) for i in k.split(',') ])))
    for z in [1,5]:
        tot = 0
        for s,k in data:
            k = k * z
            s2 = s
            for _ in range(z-1):
                s += '?'+s2
            x = check_strings(s,k)
            tot += x
        print(tot) 
