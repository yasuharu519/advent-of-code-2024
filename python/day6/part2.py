# coding: utf-8
import sys

def main():
    lines = [list(x.strip()) for x in sys.stdin.readlines()]
    m = len(lines)
    n = len(lines[0])
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d = 0

    x, y = 0, 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "^":
                x, y = (i, j)
                break
    sx, sy = x, y

    def detect_loop(x, y, d) -> bool:
        flags = [[0] * n for _ in range(m)]

        while 0 <= x < m and 0 <= y < n:
            if (flags[x][y] & (1 << d)) != 0:
                return True
            flags[x][y] |= 1 << d
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            while 0 <= nx < m and 0 <= ny < n and lines[nx][ny] == "#":
                d = (d + 1) % 4
                dx, dy = directions[d]
                nx, ny = x + dx, y + dy
            x, y = nx, ny
        return False

    # 候補を出しておく
    candidates = set()
    while 0 <= x < m and 0 <= y < n:
        if lines[x][y] == ".":
            candidates.add((x, y))
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy

        if 0 <= nx < m and 0 <= ny < n:
            while lines[nx][ny] == "#":
                d = (d + 1) % 4
                dx, dy = directions[d]
                nx, ny = x + dx, y + dy
            x, y = nx, ny
        else:
            break
    
    print("candidates num: ", len(candidates))
    
    # 各候補ごとに絞り込み
    result = 0
    for ox, oy in list(candidates):
        lines[ox][oy] = "#"
        if detect_loop(sx, sy, 0):
            result += 1
        lines[ox][oy] = "."

    print(result)

if __name__ == "__main__":
    main()