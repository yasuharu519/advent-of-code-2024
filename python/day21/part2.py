import sys
from collections import deque
from itertools import product
from functools import cache

directional_buttons = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}

def neighbors_dir(x, y):
    directions = [(-1, 0, "^"), (1, 0, "v"), (0, -1, "<"), (0, 1, ">")]
    for dx, dy, d in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 2 and 0 <= ny < 3 and (nx, ny) != (0, 0):
            yield nx, ny, d

num_buttons = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}

def neighbors_num(x, y):
    directions = [(-1, 0, "^"), (1, 0, "v"), (0, -1, "<"), (0, 1, ">")]
    for dx, dy, d in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 3 and (nx, ny) != (3, 0):
            yield nx, ny, d

def precomputed_pat(button_map, neighbor_func):
    dp = {}
    all_buttons = list(button_map.keys())

    for start_btn in all_buttons:
        for end_btn in all_buttons:
            if start_btn == end_btn:
                dp[(start_btn, end_btn)] = ["A"]
                continue

            sx, sy = button_map[start_btn]
            optimal_length = float('inf')
            candidates = []
            queue = deque([(sx, sy, "", set([(sx, sy)]))])
            while queue:
                x, y, cmd, path = queue.popleft()
                if (x, y) == button_map[end_btn]:
                    if len(cmd) <= optimal_length:
                        optimal_length = len(cmd)
                        candidates.append(cmd + "A")
                        continue
                for nx, ny, d in neighbor_func(x, y):
                    if (nx, ny) not in path:
                        queue.append((nx, ny, cmd + d, path | {(nx, ny)}))
            dp[(start_btn, end_btn)] = candidates[:]
    return dp

dp_dir_ops = precomputed_pat(directional_buttons, neighbors_dir)
dp_num_ops = precomputed_pat(num_buttons, neighbors_num)
dp_dir_length = {k: len(v[0]) for k,v in dp_dir_ops.items()}

def solve(code: str, dp: dict):
    with_prefix = "A" + code
    options = [dp[tuple(with_prefix[i:i+2])] for i in range(len(with_prefix)-1)]

    candidates = ["".join(x) for x in product(*options)]
    min_length = min(map(len, candidates))
    return list(filter(lambda x: len(x) == min_length, candidates))

def numeric_value_of_code(code):
    digits = "".join([c for c in code if c.isdigit()])
    if not digits:
        return 0
    return int(digits)

@cache
def compute_length(seq, depth=25):
    if depth == 1:
        return sum(dp_dir_length[(x, y)] for x, y in zip("A" + seq, seq))
    length = 0
    for x, y in zip("A" + seq, seq):
        length += min(compute_length(subsec, depth - 1) for subsec in dp_dir_ops[(x, y)])
    return length


def main():
    codes = [line.strip() for line in sys.stdin.readlines()]
    total_complexity = 0

    for code in codes:
        print(code)
        inputs = solve(code, dp_num_ops)
        cost = min(map(compute_length, inputs))
        val = numeric_value_of_code(code)
        complexity = cost * val
        print(f"Code={code}, top-presses={cost}, value={val}, complexity={complexity}")
        total_complexity += complexity

    print("Sum of complexities =", total_complexity)

if __name__ == "__main__":
    main()

