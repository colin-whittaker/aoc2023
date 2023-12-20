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
        case '%':
            if not v:
                s = (nodes[recv]['s']+1)%2
                nodes[recv]['s'] = s
                for o in nodes[recv]['o']:
                    pulses.append((recv,o,s))
        case '&':
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
        if send[0] in '%&':
            t = send[0]
            send = send[1:]
        else:
            t = 'b'
        nodes[send] = {}
        nodes[send]['t'] = t
        nodes[send]['o'] = recv.split(', ')
        if t == '&':
            nodes[send]['i'] = {}
        if t == '%':
            nodes[send]['s'] = 0
    for node in nodes:
        for o in nodes[node]['o']:
            if o in nodes and nodes[o]['t'] == '&':
                nodes[o]['i'][node] = 0
            elif o == 'rx':
                special = node

    inputs = copy.deepcopy(nodes[special]['i'])
    count,low,high = 0,0,0
    while True:
        pulses = [('button','broadcaster',0)]
        count += 1
        while pulses:
            send,recv,v = pulses.pop(0)
            if v:
                high +=1
            else:
                low  +=1
            if recv == special and v == 1 and inputs[send] == 0:
                inputs[send] = count
            process_pulse(send,recv,v)
        if count == 1000:
            print(low*high)
        if 0 not in inputs.values():
            break
    print(math.lcm(*inputs.values()) )
