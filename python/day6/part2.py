# coding: utf-8
import sys

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_start_coord(lines):
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "^":
                return (i, j)
    return -1, -1

def detect_loop(x, y, d, lines, passed) -> bool:
    m = len(passed)
    n = len(passed[0])
    local_passed = [[0] * n for _ in range(m)]

    while 0 <= x < m and 0 <= y < n:
        if local_passed[x][y] & (1 << d) or passed[x][y] & (1 << d):
            return True
        local_passed[x][y] |= (1 << d | passed[x][y])
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        while 0 <= nx < m and 0 <= ny < n and lines[nx][ny] == "#":
            d = (d + 1) % 4
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
        x, y = nx, ny
    return False

def main():
    lines = [list(x.strip()) for x in sys.stdin.readlines()]
    m = len(lines)
    n = len(lines[0])
    
    d = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    x, y = get_start_coord(lines)
    passed = [[0] * n for _ in range(m)]

    obstacles = 0

    # 候補を出しておく
    while 0 <= x < m and 0 <= y < n:
        passed[x][y] |= 1 << d
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy

        if 0 <= nx < m and 0 <= ny < n:
            while lines[nx][ny] == "#":
                d = (d + 1) % 4
                dx, dy = directions[d]
                nx, ny = x + dx, y + dy
            lines[nx][ny] = "#"
            
            # 障害物を配置したときにループになるか試す
            if passed[nx][ny] == 0 and detect_loop(x, y, (d + 1) % 4, lines, passed):
                obstacles += 1
            lines[nx][ny] = "."
            x, y = nx, ny
        else:
            break
    
    print(obstacles)

if __name__ == "__main__":
    main()