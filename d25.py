#!/usr/bin/env python3.10
import sys
import networkx as nx
import itertools

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    g = nx.Graph()
    for line in lines:
        nodes = line.replace(':', ' ').split()
        for dest in nodes[1:]:
            g.add_edge(nodes[0],dest,capacity=1)
    for a,b in itertools.combinations(g.nodes(),2):
        cut_size, partition = nx.minimum_cut(g,a,b)
        if cut_size == 3:
            print(len(partition[0])*len(partition[1]))
            break
