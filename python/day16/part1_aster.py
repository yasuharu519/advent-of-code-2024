import sys
import heapq

def manhattan_distance(x1, y1, x2, y2, d):
    return abs(x1 - x2) + abs(y1 - y2) + (1000 if d == 2 or d == 3 else 0)

def main():
    grid = [list(line.strip()) for line in sys.stdin.readlines()]
    m = len(grid)
    n = len(grid[0])

    dp = [[[float("inf")] * 4 for _ in range(n)] for _ in range(m)]

    # スタート地点を検索
    sx, sy = (0, 0)
    ex, ey = (0, 0)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                sx, sy = i, j
                grid[i][j] = "."
            if grid[i][j] == "E":
                ex, ey = i, j
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # N, E, S, W
    heap = [(manhattan_distance(sx, sy, ex, ey, 1), 0, sx, sy, 1)]
    steps = 0
    while heap:
        f, g, x, y, d= heapq.heappop(heap)
        steps += 1
        if grid[x][y] == "E":
            print(f"Steps: {steps}")
            print(f"Points: {g}")
            return
        if dp[x][y][d] <= g:
            continue
        dp[x][y][d] = g

        # 一歩進む
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
            new_g = g + 1
            heapq.heappush(heap, (new_g + manhattan_distance(nx, ny, ex, ey, d), new_g, nx, ny, d))

        # 回転
        for rotate in [-1, 1]:
            new_d = (d + rotate) % 4
            new_g = g + 1000
            heapq.heappush(heap, (new_g + manhattan_distance(x, y, ex, ey, new_d), new_g, x, y, new_d))
    
    print(-1)
    return

if __name__ == "__main__":
    main()