import sys
from typing import Tuple, List
from collections import deque
import heapq
from dataclasses import dataclass

@dataclass
class State:
    num_pos: Tuple[int, int]
    dir1_pos: Tuple[int, int]
    dir2_pos: Tuple[int, int]
    codes: str

def target_pos_in_num_pad(target_num) -> Tuple[int, int]:
    """
    数字のキーパッドの中で、指定された数字の位置を返す
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    """
    if target_num == "A":
        return (3, 2)
    elif target_num == "0":
        return (3, 1)
    else:
        i = int(target_num)
        row = (9 - i) // 3
        col = 2 if i % 3 == 0 else i % 3 - 1
        return (row, col)

def target_pos_in_dir_pad(target_char) -> Tuple[int, int]:
    """
    方向のキーパッドの中で、指定された文字の位置を返す
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """
    match target_char:
        case "^":
            return (0, 1)
        case "A":
            return (0, 2)
        case "<":
            return (1, 0)
        case "v":
            return (1, 1)
        case ">":
            return (1, 2)
        case _:
            raise ValueError(f"Invalid target character: {target_char}")

def find_shortest_paths_in_num_pad(num_pos: Tuple[int, int], next_num: str) -> List[Tuple[Tuple[int, int], str]]:
    """
    数字のキーパッドの中で最短距離を見つけて、その際の移動に必要な操作をすべて返す
    """
    target_pos = target_pos_in_num_pad(next_num)
    heap = []
    heapq.heappush(heap, (0, num_pos, "", set([num_pos])))
    results = []

    while heap:
        cost, pos, path, passed = heapq.heappop(heap)
        if pos == target_pos:
            if not results:
                results.append((pos, path + "A"))
            elif len(path) + 1 == len(results[0][1]):
                results.append((pos, path + "A"))
            else:
                break
        for dx, dy, s in [(-1, 0, "^"), (0, 1, ">"), (1, 0, "v"), (0, -1, "<")]:
            nx, ny = pos[0] + dx, pos[1] + dy
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 3 or (nx, ny) == (3, 0):
                continue
            if (nx, ny) in passed:
                continue
            heapq.heappush(heap, (cost + 1, (nx, ny), path + s, passed | set([(nx, ny)])))
    return results

def find_all_paths_in_num_pad(pos: Tuple[int, int], chars: str) -> List[str]:
    result = []
    queue = deque()
    queue.append((pos, chars, ""))
    while queue:
        p, rest, path = queue.popleft()
        if rest == "":
            result.append(path)
            continue
        c = rest[0]
        for np, cs in find_shortest_paths_in_num_pad(p, c):
            queue.append((np, rest[1:], path + cs))
    return result

def find_shortest_paths_in_dir_pad(pos: Tuple[int, int], next_char: str) -> List[Tuple[Tuple[int, int], str]]:
    """
    方向のキーパッドの中で複数のパスを探索
    """
    target_pos = target_pos_in_dir_pad(next_char)
    heap = []
    heapq.heappush(heap, (0, pos, "", set([pos])))
    results = []

    while heap:
        cost, pos, path, passed = heapq.heappop(heap)
        if pos == target_pos:
            if not results:
                results.append((pos, path + "A"))
            elif len(path) + 1 == len(results[0][1]):
                results.append((pos, path + "A"))
            else:
                break
        for dx, dy, s in [(-1, 0, "^"), (0, 1, ">"), (1, 0, "v"), (0, -1, "<")]:
            nx, ny = pos[0] + dx, pos[1] + dy
            if nx < 0 or nx >= 2 or ny < 0 or ny >= 3 or (nx, ny) == (0, 0):
                continue
            if (nx, ny) in passed:
                continue
            heapq.heappush(heap, (cost + 1, (nx, ny), path + s, passed | set([(nx, ny)])))
    return results

def find_all_paths_in_dir1(pos: Tuple[int, int], chars: str) -> List[str]:
    """
    与えられた文字列に対して、可能な全てのパスを探索する。
    """
    result = []
    queue = deque()
    queue.append((pos, chars, ""))

    while queue:
        p, rest, path = queue.popleft()
        if rest == "":
            result.append(path)
            continue
        c = rest[0]
        for np, cs in find_shortest_paths_in_dir_pad(p, c):
            queue.append((np, rest[1:], path + cs))
    return result

def find_path_in_dir2(pos: Tuple[int, int], chars: str) -> str:
    result = ""
    for c in chars:
        pos, cs = find_shortest_in_dir_pad(pos, c)
        result += cs
    return result


def find_shortest_in_dir_pad(pos: Tuple[int, int], next_char: str) -> Tuple[Tuple[int, int], str]:
    """
    方向のキーパッドの中で最短のパスを探索
    """
    target_pos = target_pos_in_dir_pad(next_char)
    queue = deque()
    queue.append((pos, ""))
    passed = set()

    while queue:
        pos, path = queue.popleft()
        if pos == target_pos:
            return pos, path + "A"
        if pos in passed:
            continue
        passed.add(pos)
        for dx, dy, s in [(-1, 0, "^"), (0, 1, ">"), (1, 0, "v"), (0, -1, "<")]:
            nx, ny = pos[0] + dx, pos[1] + dy
            if nx < 0 or nx >= 2 or ny < 0 or ny >= 3 or (nx, ny) == (0, 0):
                continue
            if (nx, ny) in passed:
                continue
            queue.append(((nx, ny), path + s))
    raise ValueError("No path found")


def solve(state: State, num_codes: str) -> str:
    results = []

    for num_pad_path in find_all_paths_in_num_pad(state.num_pos, num_codes):
        for dir1_path in find_all_paths_in_dir1(state.dir1_pos, num_pad_path):
            dir2_path = find_path_in_dir2(state.dir2_pos, dir1_path)
            heapq.heappush(results, (len(dir2_path), dir2_path, dir1_path, num_pad_path))
    res = heapq.heappop(results)

    print(f"Codes: {num_codes}")
    print(f"Num path: {res[3]}")
    print(f"Dir1 path: {res[2]}")
    print(f"Dir2 path: {res[1]}, {len(res[1])}")
    return res[1]

def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    result = 0

    for line in lines:
        state = State((3, 2), (0, 2), (0, 2), "")
        codes = solve(state, line)
        num = int("".join([x for x in list(line) if x.isdigit()]))
        print(f"{num} * {len(codes)}")
        result += num * len(codes)
    print(result)


if __name__ == "__main__":
    main()
