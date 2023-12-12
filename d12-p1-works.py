#!/usr/bin/env python3.10
import sys

def check_strings(s,k):
    res = 0
    key = k
    k = [ int(i) for i in k.split(',') ]
    for v in s:
        if (v,key) in cache:
            continue
        #print(s,k)
        valid = True
        i,j = 0,0
        while valid:
            t = v[i:].find('#')
            if t == -1:
                res += 1
                valid = False
                break
            t += i
            #print(v,t,i,j,k[j])
            if len(v[t:]) < k[j]:
              #  print('len fail')
                res += 1
                valid = False
            elif len(v[t:]) > k[j] and v[t+k[j]] == '#':
                res += 1
                valid = False
            elif j < len(k)-1 and (len(v[t:]) == k[j] or v[t+k[j]] == '#'):
               # print('gap fail')
                res += 1
                valid = False
            elif '.' in v[t:t+k[j]] :
                #print('match fail')
                res += 1
                valid = False
            else:
               # print('still valid')
                i = t+k[j]
                j += 1
                if j == len(k):
                    if '#' in v[i:]:
                        res += 1
                        valid = False
                    else:
                        break
                #    print('out of k')
        if valid:
            cache.add((v,key))
            #print(v,valid)
    return len(s) - res

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    data = []
    for line in lines:
        data.append(line.split())
    tot = 0
    cache = set()
    for k,v in data:
        s = [k]
        res = []
        #print(s,v)
        while len(s):
            t = s.pop(0)
            if '?' in t:
                i = t.find('?')
                s.append(t[:i]+'.'+t[i+1:])
                s.append(t[:i]+'#'+t[i+1:])
            else:
                res.append(t)
        #print(res)
        x = check_strings(res,v)
        tot += x
        print(k,v,x,tot)
    print(tot) 
