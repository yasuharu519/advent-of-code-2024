import sys
from typing import Set
from functools import cache

def check(target: str, color_set: Set[str]) -> bool:
    l = list(color_set)
    n = len(l)
    counter = 0

    @cache
    def dfs(rest: str) -> int:
        nonlocal counter
        if rest == "":
            return 1
        
        count = 0
        for i in range(n):
            if rest.startswith(l[i]):
                count += dfs(rest[len(l[i]):])
        return count

    res = dfs(target)
    print(target, res)
    return res

def main():
    lines = sys.stdin.readlines()
    color = [line.strip() for line in lines[0].split(",")]
    color_set = set(color)

    count = 0
    for line in lines[2:]:
        print(f"check {line}")
        line = line.strip()
        count += check(line, color_set)
    print(count)

if __name__ == "__main__":
    main()