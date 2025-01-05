import sys
import heapq

def main():
    grid = [list(line.strip()) for line in sys.stdin.readlines()]
    m = len(grid)
    n = len(grid[0])

    dp = [[[float("inf")] * 4 for _ in range(n)] for _ in range(m)]

    # スタート地点を検索
    sx, sy = (0, 0)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                sx, sy = i, j
                grid[i][j] = "."
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # N, E, S, W
    heap = [(0, sx, sy, 1)]
    while heap:
        cost, x, y, d= heapq.heappop(heap)
        if grid[x][y] == "E":
            print(cost)
            return
        if dp[x][y][d] <= cost:
            continue
        dp[x][y][d] = cost

        # 一歩進む
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
            heapq.heappush(heap, (cost + 1, nx, ny, d))

        # 回転
        heapq.heappush(heap, (cost + 1000, x, y, (d + 1) % 4))
        heapq.heappush(heap, (cost + 1000, x, y, (d - 1) % 4))
    
    print(-1)
    return

if __name__ == "__main__":
    main()