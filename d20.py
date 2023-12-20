#!/usr/bin/env python3.10
import sys
import copy
import math

def process_pulse(send,recv,v):
    if recv not in nodes:
        return
    match nodes[recv]['t']:
        case 'b':
            for o in nodes[recv]['o']:
                pulses.append((recv,o,0))
        case 'f':
            if v == 0:
                s = nodes[recv]['s']
                s = (s+1)%2
                nodes[recv]['s'] = s
                for o in nodes[recv]['o']:
                    pulses.append((recv,o,s))
        case 'c':
            nodes[recv]['i'][send] = v
            v = 1 if 0 in nodes[recv]['i'].values() else 0
            for o in nodes[recv]['o']:
                pulses.append((recv,o,v))

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    nodes = {}
    for line in lines:
        send,recv = line.split(' -> ')
        recv = recv.split(', ')
        if '%' == send[0]:
            t = 'f'
            send = send[1:]
        elif '&' == send[0]:
            t = 'c'
            send = send[1:]
        else:
            t = 'b'
        nodes[send] = {}
        nodes[send]['t'] = t
        nodes[send]['o'] = recv
        if t  == 'c':
            nodes[send]['i'] = {}
        if t == 'f':
            nodes[send]['s'] = 0
    for node in nodes:
        for o in nodes[node]['o']:
            if o in nodes and nodes[o]['t'] == 'c':
                nodes[o]['i'][node] = 0
            if o == 'rx':
                special = node

    nodes2 = copy.deepcopy(nodes)
    low,high = 0,0
    for _ in range(1000):
        pulses = [('button','broadcaster',0)]
        while pulses:
            send,recv,v = pulses.pop(0)
            if v:
                high +=1
            else:
                low  +=1
            process_pulse(send,recv,v)
                       
    print(low*high)

    inputs = copy.deepcopy(nodes[special]['i'])
    count = 0
    rx = False
    nodes = nodes2
    while not rx:
        pulses = [('button','broadcaster',0)]
        count += 1
        while pulses:
            send,recv,v = pulses.pop(0)
            if recv == special and v == 1 and inputs[send] == 0:
                inputs[send] = count
            if 0 not in inputs.values():
                rx = True
            process_pulse(send,recv,v)
    print(math.lcm(*inputs.values()) )
