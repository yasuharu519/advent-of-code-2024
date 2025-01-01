# coding: utf-8
import sys
from functools import reduce

MAP_W = 101
MAP_H = 103

def get_quad(px, py):
    """
    px, py がどの象限に属するかを返す
    """
    if px < MAP_W // 2:
        if py < MAP_H // 2:
            return 0
        else:
            return 3
    else:
        if py < MAP_H // 2:
            return 1
        else:
            return 2

def main():
    lines = [line.strip() for line in sys.stdin.readlines()]

    quads = [0] * 4
    for line in lines:
        pos, vec = line.strip().split(" ")
        pos, vec = pos[2:], vec[2:]
        px, py = map(int, pos.split(","))
        vx, vy = map(int, vec.split(","))

        # position after 100 seconds
        nx, ny = px + 100 * vx, py + 100 * vy
        nx, ny = nx % MAP_W, ny % MAP_H
        
        if nx == MAP_W // 2 or ny == MAP_H // 2:
            continue
        quads[get_quad(nx, ny)] += 1
    print(reduce(lambda x, y: x * y, quads))

if __name__ == "__main__":
    main()