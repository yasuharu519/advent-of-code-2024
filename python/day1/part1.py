#!/usr/bin/env python3
import sys
import heapq

def main():
    lines = sys.stdin.readlines()
    left, right = [], []
    for line in lines:
        a, b = map(int, line.split())
        heapq.heappush(left, a)
        heapq.heappush(right, b)
    result = 0
    while left and right:
        a, b = heapq.heappop(left), heapq.heappop(right)
        result += abs(a - b)
    print(result)

if __name__ == "__main__":
    main()