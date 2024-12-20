# coding: utf-8
import sys
from functools import cache

def main():
    lines = [list(map(int, list(line.strip()))) for line in sys.stdin.readlines()]
    print(lines)
    m = len(lines)
    n = len(lines[0])

    @cache
    def dfs(x, y) -> int:
        v = int(lines[x][y])
        if v == 9:
            return 1
        
        result = 0
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if lines[nx][ny] == v + 1:
                    result += dfs(nx, ny)
        return result
    
    result = 0
    for i in range(m):
        for j in range(n):
            if lines[i][j] == 0:
                res = dfs(i, j)
                print(i, j, res)
                result += res

    print(result)


if __name__ == "__main__":
    main()