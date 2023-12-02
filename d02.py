#!/usr/bin/env python3.10
import sys

def check_game1(game):
    for show in game:
        for x,y in show.items():
            if x == 'red' and y >12:
                return False
            if x == 'green' and y >13:
                return False
            if x == 'blue' and y >14:
                return False
    return True

def power_game(game):
    r,g,b = 0,0,0
    for show in game:
        for x,y in show.items():
            if x == 'red':
                r = max(r,y)
            if x == 'green':
                g = max(g,y)
            if x == 'blue':
                b = max(b,y)
    return r*g*b

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    games = {}
    for line in lines:
        game,line = line.split(':')
        game = int(game.split(' ')[1])
        games[game] = []
        for x in line.split(';'):
            show = {}
            for y in x.split(','):
                n,c = y.strip().split(' ')
                show[c] = int(n)
            games[game].append(show)

    tot = 0
    tot2 = 0
    for game in games.keys():
        if check_game1(games[game]):
            tot += game
        tot2 += power_game(games[game])
    print(tot)
    print(tot2)
