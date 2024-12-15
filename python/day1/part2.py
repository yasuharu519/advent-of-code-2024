#!/usr/bin/env python3
import sys
from collections import defaultdict

def main():
    lines = sys.stdin.readlines()
    left, right = defaultdict(int), defaultdict(int)
    for line in lines:
        a, b = map(int, line.split())
        left[a] += 1
        right[b] += 1
    result = 0
    for k,v in left.items():
        result += k * v * right[k]
    print(result)

if __name__ == "__main__":
    main()