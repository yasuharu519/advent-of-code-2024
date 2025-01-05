# coding: utf-8
import os
import time
import sys
import heapq
from collections import defaultdict

RED = "\033[31m"
RESET = "\033[0m"

def print_grid_and_path(grid, cell_on_best_routes):
    m = len(grid)
    n = len(grid[0])
    os.system("clear")

    for i in range(m):
        for j in range(n):
            if (i, j) in cell_on_best_routes:
                print(f"{RED}o{RESET}", end="")
            else:
                print(grid[i][j], end="")
        print()
    time.sleep(0.1)
    return

def main():
    grid = [list(line.strip()) for line in sys.stdin.readlines()]
    m = len(grid)
    n = len(grid[0])

    dp = [[[float("inf")] * 4 for _ in range(n)] for _ in range(m)]

    sx, sy = (0, 0)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                sx, sy = i, j
                grid[i][j] = "."
    
    # N, E, S, W
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    heap = [(0, sx, sy, 1, set([(sx, sy)]))]
    best_score = float("inf")
    cell_on_best_routes = set()

    steps = 0
    while heap:
        cost, x, y, d, path = heapq.heappop(heap)
        # print(f"cost: {cost}, x: {x}, y: {y}, d: {d}, remaining: {len(heap)}")
        steps += 1
        if steps % 5000 == 0:
            print_grid_and_path(grid, path)

        if grid[x][y] == "E":
            if best_score == float("inf"):
                best_score = cost
                cell_on_best_routes |= path
            elif best_score == cost:
                cell_on_best_routes |= path
            else:
                break
        if dp[x][y][d] < cost:
            continue
        dp[x][y][d] = cost

        # 一歩進む
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
            heapq.heappush(heap, (cost + 1, nx, ny, d, path | set([(nx, ny)])))

        # 回転
        heapq.heappush(heap, (cost + 1000, x, y, (d + 1) % 4, path))
        heapq.heappush(heap, (cost + 1000, x, y, (d - 1) % 4, path))
    

    print_grid_and_path(grid, cell_on_best_routes)
    print(f"Score: {len(cell_on_best_routes)}")
    print(f"Steps: {steps}")

if __name__ == "__main__":
    main()