#!/usr/bin/env python3.10
import sys

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    cards = []
    tot = 0
    for line in lines:
        n,line = line.split(': ')
        win,mine = line.split(' | ')
        win = set(win.strip().split())
        mine = set(mine.strip().split())
        matches = len(win.intersection(mine))
        if matches:
            tot += pow(2,matches-1)
        cards.append([1,matches])
    print(tot)
    for i,v in enumerate(cards):
        n,m = v
        if m:
            while m > 0:
                cards[i+m][0] += n
                m -= 1
    print(sum([ card[0] for card in cards]))
