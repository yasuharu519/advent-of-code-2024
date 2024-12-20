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

    # search start to end
    queue = deque([(0, start)])
    while queue:
        cost, (x, y) = queue.popleft()
        if start_to_end[x][y] <= cost:
            continue
        start_to_end[x][y] = cost
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if x <= 0 or x >= m-1 or y <= 0 or y >= n-1:
                continue
            if lines[nx][ny] == "." and start_to_end[nx][ny] > cost + 1:
                queue.append((cost + 1, (nx, ny)))

    # search end to start
    queue = deque([(0, end)])
    while queue:
        cost, (x, y) = queue.popleft()
        if end_to_start[x][y] <= cost:
            continue
        end_to_start[x][y] = cost
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if x <= 0 or x >= m-1 or y <= 0 or y >= n-1:
                continue
            if lines[nx][ny] == "." and end_to_start[nx][ny] > cost + 1:
                queue.append((cost + 1, (nx, ny)))
    
    length = start_to_end[end[0]][end[1]]
    print(length)

    def search(sx, sy) -> int:
        count = 0
        passed = set()
        queue = deque([(0, (sx, sy))])
        base_cost = start_to_end[sx][sy]
        while queue:
            cost, (x, y) = queue.popleft()
            if (x, y) in passed:
                continue
            new_cost = base_cost + cost + end_to_start[x][y]
            if new_cost <= length - 100:
                count += 1
            passed.add((x, y))
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if nx <= 0 or nx >= m-1 or ny <= 0 or ny >= n-1:
                    continue
                if (nx, ny) not in passed and cost + 1 <= 20:
                    queue.append((cost + 1, (nx, ny)))
        return count

    passed = set()
    queue = deque([start])
    count = 0
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        if (x, y) in passed:
            continue
        passed.add((x, y))
        print(f"Chekcing... {x}, {y}")
        # check shortcut
        count += search(x, y)
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