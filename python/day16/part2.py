# coding: utf-8
import sys
import heapq
from collections import defaultdict

def main():
    input_map = [list(line.strip()) for line in sys.stdin.readlines()]
    m = len(input_map)
    n = len(input_map[0])
    dp = [[[float("inf")] * 4 for _ in range(n)] for _ in range(m)]
    dp_path = defaultdict(set)

    sx, sy = (0, 0)
    for i in range(m):
        for j in range(n):
            if input_map[i][j] == "S":
                sx, sy = i, j
                input_map[i][j] = "."
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # N, E, S, W
    heap = [(0, sx, sy, 1, set([(sx, sy)]))]
    best_score = float("inf")
    cell_on_best_routes = set()
    while heap:
        cost, x, y, d, path = heapq.heappop(heap)
        print(f"cost: {cost}, x: {x}, y: {y}, d: {d}, remaining: {len(heap)}")
        if input_map[x][y] == "E":
            if best_score == float("inf"):
                print("Found route first")
                best_score = cost
                cell_on_best_routes = cell_on_best_routes.union(path)
            elif best_score == cost:
                print("Found other best route")
                cell_on_best_routes = cell_on_best_routes.union(path)
            else:
                break
        if dp[x][y][d] < cost:
            continue
        dp[x][y][d] = cost
        dp_path[(x, y, d)] = dp_path[(x, y, d)].union(path)

        # 一歩進む
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and input_map[nx][ny] != "#":
            heapq.heappush(heap, (cost + 1, nx, ny, d, path | set([(nx, ny)])))
        # 回転
        heapq.heappush(heap, (cost + 1000, x, y, (d + 1) % 4, path))
        heapq.heappush(heap, (cost + 1000, x, y, (d - 1) % 4, path))
    
    print(len(cell_on_best_routes))
    for i in range(m):
        for j in range(n):
            if (i, j) in cell_on_best_routes:
                print("o", end="")
            else:
                print(input_map[i][j], end="")
        print()
    return


if __name__ == "__main__":
    main()