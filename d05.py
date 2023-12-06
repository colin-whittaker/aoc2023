#!/usr/bin/env python3.10
import sys

def apply_map(m, seedr):
    ans =[]
    for src in m:
        dest,r = m[src]
        src_end = src+r
        new = []
        while seedr:
            x,y = seedr.pop()
            before = (x,min(y,src))
            middle = (max(x,src),min(src_end,y))
            after  = (max(src_end,x),y)
            if before[1] > before[0]:
                new.append(before)
            if middle[1] > middle[0]:
                ans.append((middle[0]-src+dest, middle[1]-src+dest))
            if after[1] > after[0]:
                new.append(after)
        seedr = new
    return ans+seedr

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    seeds = [ int(x) for x in lines.pop(0).split(': ')[1].split() ]
    maps = []
    tables = {}
    for line in lines:
        if line == '':
            continue
        if '-' in line:
            m = line.split('-')[0]
            maps.append(m)
            tables[m] = {}
        else:
            dest, src, r = [ int(x) for x in line.split()] 
            tables[m][src] = (dest, r)

    res = []
    for ans in seeds:
        for m in maps:
            for src in tables[m]:
                dest,r = tables[m][src]
                if src <= ans and ans < src+r:
                    ans = ans - src + dest
                    break
        res.append(ans)
    print(min(res))
    res=[]
    seeds = list(zip(seeds[::2],seeds[1::2]))
    for x,r in seeds:
        seedr = [(x,x+r)]
        for m in maps:
            seedr = apply_map(tables[m],seedr)
        res.append(min(seedr)[0])
    print(min(res))
