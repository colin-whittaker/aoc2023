#!/usr/bin/env python3.10
import sys
from functools import cmp_to_key
from collections import Counter

def hand_type(a,wild):
    ac = Counter(a)
    acm = max(ac.values())
    wild = wild and 'J' in a
    match acm:
        case 5:
            return 6
        case 4:
            return 6 if wild else 5
        case 1:
            return 1 if wild else 0
        case 3:
            if len(ac.values()) == 2:
                return 6 if wild else 4
            return 5 if wild else 3
        case 2:
            if len(ac.values()) == 3:
                return 3+ac['J'] if wild else 2
            return 3 if wild else 1

def card_2_value(x,wild):
    cards = '0J23456789T1QKA' if wild else '0123456789TJQKA'
    return cards.index(x)

def cmp_hand_wild(a,b):
    return cmp_hand(a,b,True)

def cmp_hand(a,b,wild=False):
    if a == b:
        return 0
    t = hand_type(a,wild) - hand_type(b,wild)
    if t != 0 :
        return t
    for i in range(5):
        if a[i] == b[i]:
            continue
        return card_2_value(a[i],wild) - card_2_value(b[i],wild)

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    hands = {}
    for line in lines:
        hand,bid = line.split()
        hands[hand] = int(bid)
    res = sorted(hands.keys(), key=cmp_to_key(cmp_hand))
    print( sum ((i)*hands[v] for i,v in enumerate(res,1)))
    res = sorted(hands.keys(), key=cmp_to_key(cmp_hand_wild))
    print( sum ((i)*hands[v] for i,v in enumerate(res,1)))
