import sys
from typing import Set
from functools import cache

def check(target: str, color_set: Set[str]) -> bool:
    l = list(color_set)
    n = len(l)

    @cache
    def dfs(rest: str) -> bool:
        if rest == "":
            return True
        for i in range(n):
            if rest.startswith(l[i]):
                if dfs(rest[len(l[i]):]):
                    return True
        return False

    return dfs(target)

def main():
    lines = sys.stdin.readlines()
    color = [line.strip() for line in lines[0].split(",")]
    color_set = set(color)

    print(len([line for line in lines[2:] if check(line.strip(), color_set)]))

if __name__ == "__main__":
    main()