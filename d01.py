#!/usr/bin/env python3.10
import re
import sys

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    total = 0
    replace = {'one':'o1e','two':'t2o','three':'t3ree','four':'4our','five':'5ive','six':'6ix','seven':'7even','eight':'e8ght','nine':'n9ne'}
    for line in lines:
        newa = line
        for pattern in replace.keys():
            newa = re.sub(pattern,replace[pattern],newa)
        new = re.findall('[0-9]',newa)
        total += int(new[0]+new[-1])
    print(total)
