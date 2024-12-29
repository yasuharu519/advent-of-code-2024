import sys
from functools import cache

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    lines = [list(map(int, list(line.strip()))) for line in sys.stdin.readlines()]
    m = len(lines)
    n = len(lines[0])

    @cache
    def dfs(x, y) -> int:
        v = int(lines[x][y])
        if v == 9:
            return 1
        result = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and lines[nx][ny] == v + 1:
                result += dfs(nx, ny)
        return result
    
    result = 0
    for i in range(m):
        for j in range(n):
            if lines[i][j] == 0:
                result += dfs(i, j)
    print(result)


if __name__ == "__main__":
    main()