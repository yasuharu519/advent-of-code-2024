import sys
from collections import deque

def main():
    lines = [list(line.strip()) for line in sys.stdin.readlines()]
    start, end = (0, 0), (0, 0)

    m = len(lines)
    n = len(lines[0])

    for i in range(m):
        for j in range(n):
            if lines[i][j] == "S":
                start = (i, j)
                lines[i][j] = "."
            elif lines[i][j] == "E":
                end = (i, j)
                lines[i][j] = "."
    
    start_to_end = [[float('inf') for _ in range(n)] for _ in range(m)]
    end_to_start = [[float('inf') for _ in range(n)] for _ in range(m)]

    def search(start: tuple) -> list[list[int]]:
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        # search start to end
        queue = deque([(0, start)])
        while queue:
            cost, (x, y) = queue.popleft()
            if dp[x][y] <= cost:
                continue
            dp[x][y] = cost
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if x <= 0 or x >= m-1 or y <= 0 or y >= n-1:
                    continue
                if lines[nx][ny] == "." and dp[nx][ny] > cost + 1:
                    queue.append((cost + 1, (nx, ny)))
        return dp
    
    start_to_end = search(start)
    end_to_start = search(end)
    
    length = start_to_end[end[0]][end[1]]
    print(length)

    passed = set()
    queue = deque([start])
    count = 0
    short_cut = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        if (x, y) in passed:
            continue
        passed.add((x, y))
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            # check if there is a shortcut
            if lines[x+dx][y+dy] == "#" and \
                0 <= x+2*dx < m and 0 <= y+2*dy < n and \
                    lines[x+2*dx][y+2*dy] == "." and \
                        (x+dx, y+dy) not in short_cut:
                short_cut.add((x+dx, y+dy))
                new_length = start_to_end[x][y] + 2 + end_to_start[x+2*dx][y+2*dy]
                if new_length <= length - 100:
                    count += 1
        # move
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if lines[nx][ny] == "." and (nx, ny) not in passed:
                queue.append((nx, ny))
    print(count)

if __name__ == "__main__":
    main()