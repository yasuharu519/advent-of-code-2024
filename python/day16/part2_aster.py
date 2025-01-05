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
    time.sleep(1)
    return

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def main():
    grid = [list(line.strip()) for line in sys.stdin.readlines()]
    m = len(grid)
    n = len(grid[0])

    dp = [[[float("inf")] * 4 for _ in range(n)] for _ in range(m)]

    sx, sy = (0, 0)
    ex, ey = (0, 0)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                sx, sy = i, j
                grid[i][j] = "."
            elif grid[i][j] == "E":
                ex, ey = i, j
    
    # N, E, S, W
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # かかった
    heap = [(0 + manhattan_distance(sx, sy, ex, ey), 0, sx, sy, 1, set([(sx, sy)]))]
    best_score = float("inf")
    cell_on_best_routes = set()

    steps = 0
    while heap:
        f, g, x, y, d, path = heapq.heappop(heap)
        steps += 1
        if steps % 5000 == 0:
            print_grid_and_path(grid, path)

        if grid[x][y] == "E":
            if best_score == float("inf"):
                best_score = g
                cell_on_best_routes |= path
            elif best_score == g:
                cell_on_best_routes |= path
            else:
                if g > best_score:
                    break
        if dp[x][y][d] < g:
            continue
        dp[x][y][d] = g

        # 一歩進む
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
            new_g = g + 1
            # if new_g <= dp[nx][ny][d]:
            #     dp[nx][ny][d] = new_g
            new_h = manhattan_distance(nx, ny, ex, ey)
            heapq.heappush(heap, (new_g + new_h, new_g, nx, ny, d, path | set([(nx, ny)])))

        # 回転
        for rorate in [-1, 1]:
            nd = (d + rorate) % 4
            new_g = g + 1000
            # if new_g <= dp[x][y][nd]:
            #     dp[x][y][nd] = new_g
            new_h = manhattan_distance(x, y, ex, ey)
            heapq.heappush(heap, (new_g + new_h, new_g, x, y, nd, path))

    print_grid_and_path(grid, cell_on_best_routes)
    print(f"Score: {len(cell_on_best_routes)}")
    print(f"Steps: {steps}")

if __name__ == "__main__":
    main()