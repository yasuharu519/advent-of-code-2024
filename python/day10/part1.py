import sys
from collections import deque
from functools import cache

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    lines = [list(map(int, list(line.strip()))) for line in sys.stdin.readlines()]
    m = len(lines)
    n = len(lines[0])

    def count(x, y) -> set:
        queue = deque([(0, x, y)])
        reached = set()
        while queue:
            c, xx, yy = queue.popleft()
            if c == 9:
                reached.add((xx, yy))
                continue
            for dx, dy in directions:
                nx, ny = xx + dx, yy + dy
                if 0 <= nx < m and 0 <= ny < n and lines[nx][ny] == c + 1:
                    queue.append((c + 1, nx, ny))
        return len(reached)
    
    result = 0
    for i in range(m):
        for j in range(n):
            if lines[i][j] == 0:
                result += count(i, j)
    print(result)


if __name__ == "__main__":
    main()