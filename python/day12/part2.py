import sys
from collections import defaultdict, deque
from typing import Tuple, List

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def main():
    gardens = [list(line.strip()) for line in sys.stdin.readlines()]

    m = len(gardens)
    n = len(gardens[0])

    def count_same_plants(x, y) -> List[Tuple[int, int]]:
        """
        (x, y) で指定された grid と隣接している同じ植物のセルを探す
        """
        c = gardens[x][y]
        queue = deque([(x, y)])

        cells = set()
        cells.add((x, y))

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in cells and gardens[nx][ny] == c:
                        queue.append((nx, ny))
                        cells.add((nx, ny))
        return cells

    def merge_fence(segments):
        """
        [(s1, e1), (s2, e2), ...] のようなセグメントが渡されるので、重なっている部分をマージする
        """
        segments.sort()
        rest = deque(segments[:])
        merged = []

        while rest:
            s, e = rest.popleft()
            while rest and rest[0][0] <= e:
                _, e = rest.popleft()
            merged.append((s, e))
        return merged
    
    def count_fences(cells):
        """
        渡されたセル情報から、周囲の fence の数を数える
        """
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

        side_count = 0
        for l in up.values():
            side_count += len(merge_fence(l))
        for l in bottom.values():
            side_count += len(merge_fence(l))
        for l in left.values():
            side_count += len(merge_fence(l))
        for l in right.values():
            side_count += len(merge_fence(l))
        return side_count

    result = 0
    counted_segment = set()
    for i in range(m):
        for j in range(n):
            if (i, j) in counted_segment:
                continue

            plants = count_same_plants(i, j)
            counted_segment.update(plants)

            fence_num = count_fences(plants)
            result += len(plants) * fence_num
            print(gardens[i][j], len(plants), fence_num)
    print(result)


if __name__ == "__main__":
    main()