# coding: utf-8

import sys

def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    m = len(lines)
    n = len(lines[0])
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0

    x, y = 0, 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "^":
                x, y = (i, j)
                break
    passed = set()
    count = 0
    while 0 <= x < m and 0 <= y < n:
        if (x, y) not in passed:
            count += 1
        passed.add((x, y))
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if lines[nx][ny] == "#":
                direction = (direction + 1) % 4
                dx, dy = directions[direction]
                nx, ny = x + dx, y + dy
            x, y = nx, ny
        else:
            break
    print(count)

if __name__ == "__main__":
    main()