#!/usr/bin/env python3.10
import re
import sys

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    total = 0
    replace = {'one':'o1e','two':'t2','three':'3e','four':'4','five':'5e','six':'6','seven':'7n','eight':'8','nine':'9'}
    for newa in lines:
        for pattern in replace.keys():
            newa = re.sub(pattern,replace[pattern],newa)
        new = re.findall('[0-9]',newa)
        total += int(new[0]+new[-1])
    print(total)
