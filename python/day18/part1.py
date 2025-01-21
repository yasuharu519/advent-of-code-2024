import sys
from collections import deque
from typing import List

RED = "\033[31m"
RESET = "\033[0m"

MAP_W = 71
MAP_H = 71

def print_grid(dp: List[List[str]]):
    for row in dp:
        for c in row:
            if c == "o":
                print(f"{RED}o{RESET}", end="")
            else:
                print(c, end="")
        print()

def main():
    lines = sys.stdin.readlines()

    dp = [["."] * MAP_W for _ in range(MAP_H)]

    for line in lines[:1024]:
        y, x = map(int, line.strip().split(","))
        dp[x][y] = "#"

    current = (0, 0)
    queue = deque()
    queue.append((0, current, [(0, 0)]))
    passed = set()
    while queue:
        cost, (x, y), path = queue.popleft()
        if (x, y) == (MAP_W - 1, MAP_H - 1):
            # update path on grid
            for x, y in path:
                dp[x][y] = "o"
            print_grid(dp)
            print(cost)
            return
        if (x, y) in passed:
            continue
        passed.add((x, y))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < MAP_H and 0 <= ny < MAP_W and (nx, ny) not in passed and dp[nx][ny] == ".":
                queue.append((cost + 1, (nx, ny), path + [(nx, ny)]))
    print("No path found")
        
    

if __name__ == "__main__":
    main()