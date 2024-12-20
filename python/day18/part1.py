import sys
from collections import deque

MAP_W = 71
MAP_H = 71

def main():
    lines = sys.stdin.readlines()

    dp = [["."] * MAP_W for _ in range(MAP_H)]

    for line in lines[:1024]:
        y, x = map(int, line.strip().split(","))
        dp[x][y] = "#"

    for row in dp:
        print("".join(row))

    current = (0, 0)
    queue = deque()
    queue.append((0, current))
    passed = set()
    # heap = [(0, current)]
    while queue:
        cost, (x, y) = queue.popleft()
        if (x, y) == (MAP_W - 1, MAP_H - 1):
            print(cost)
            return
        if (x, y) in passed:
            continue
        passed.add((x, y))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < MAP_H and 0 <= ny < MAP_W and (nx, ny) not in passed and dp[nx][ny] == ".":
                queue.append((cost + 1, (nx, ny)))
    print("No path found")
        
    

if __name__ == "__main__":
    main()