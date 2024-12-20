# coding: utf-8
import sys
from collections import deque

def main():
    gardens = [list(line.strip()) for line in sys.stdin.readlines()]
    m = len(gardens)
    n = len(gardens[0])

    passed = set()
    def count(x, y) -> int:
        c = gardens[x][y]
        queue = deque([(x, y)])

        count = 0
        fences = 0

        while queue:
            x, y = queue.popleft()
            if gardens[x][y] != c:
                continue
            if (x, y) in passed:
                continue
            passed.add((x, y))
            count += 1
            fences += 4
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nx, ny = x + dx, y + dy
                fences -= int(0 <= nx < m and 0 <= ny < n and gardens[nx][ny] == c)
                if 0 <= nx < m and 0 <= ny < n and gardens[nx][ny] == c and (nx, ny) not in passed:
                    queue.append((nx, ny))
        print(count, fences, c)
        return count * fences

    result = 0
    for i in range(m):
        for j in range(n):
            if (i, j) in passed:
                continue
            result += count(i, j)
    print(result)


if __name__ == "__main__":
    main()