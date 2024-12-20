# coding: utf-8
import sys
from collections import defaultdict, deque
from typing import Tuple, List

def main():
    gardens = [list(line.strip()) for line in sys.stdin.readlines()]
    m = len(gardens)
    n = len(gardens[0])
    print(gardens)

    passed = set()

    def bfs(x, y) -> List[Tuple[int, int]]:
        c = gardens[x][y]
        queue = deque([(x, y)])
        passed.add((x, y))
        cells = set()
        cells.add((x, y))
        while queue:
            x, y = queue.popleft()
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in passed and gardens[nx][ny] == c:
                        passed.add((nx, ny))
                        queue.append((nx, ny))
                        cells.add((nx, ny))
        return cells
    
    def extract_edges(cells):
        up = defaultdict(list)
        bottom = defaultdict(list)
        left = defaultdict(list)
        right = defaultdict(list)
        cell_set = set(cells)
        for x, y in cells:
            if x == 0 or (x-1, y) not in cell_set:
                up[x].append((y, y+1))
            if x == m-1 or (x+1, y) not in cell_set:
                bottom[x+1].append((y, y+1))
            if y == 0 or (x, y-1) not in cell_set:
                left[y].append((x, x+1))
            if y == n-1 or (x, y+1) not in cell_set:
                right[y+1].append((x, x+1))

        def merge_segments(segments):
            print(segments)
            segments.sort()
            merged = []
            cs, ce = segments[0]
            for s, e in segments[1:]:
                if s <= ce:
                    ce = max(ce, e)
                else:
                    merged.append((cs, ce))
                    cs, ce = s, e
            merged.append((cs, ce))
            return merged
        for row in up:
            up[row] = merge_segments(up[row])
            print(f"row up: {row}, {up[row]}")
        for row in bottom:
            bottom[row] = merge_segments(bottom[row])
            print(f"row bottom: {row}, {bottom[row]}")
        for col in left:
            left[col] = merge_segments(left[col])
            print(f"col left: {col}, {left[col]}")
        for col in right:
            right[col] = merge_segments(right[col])
            print(f"col right: {col}, {right[col]}")
        
        side_count = sum(len(up[row]) for row in up) + \
            sum(len(bottom[row]) for row in bottom) + \
            sum(len(left[col]) for col in left) + \
            sum(len(right[col]) for col in right)
        return side_count

    result = 0
    for i in range(m):
        for j in range(n):
            if (i, j) in passed:
                continue
            cells = bfs(i, j)
            print(cells)
            edges = extract_edges(cells)
            result += len(cells) * edges
            print(gardens[i][j], len(cells), edges)
    print(result)


if __name__ == "__main__":
    main()