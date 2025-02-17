#!/usr/bin/env python3
import sys
from typing import List

def check(input: List[int]) -> bool:
    diff = input[1] - input[0]
    if diff >= 0:
        return all(1 <= input[i+1] - input[i] <= 3 for i in range(len(input) - 1))
    else:
        return all(-3 <= input[i+1] - input[i] <= -1 for i in range(len(input) - 1))

def main():
    lines = sys.stdin.readlines()
    counter = 0
    for line in lines:
        line = list(map(int, line.split()))
        if check(line):
            counter += 1
        else:
            for i in range(len(line)):
                if check(line[:i] + line[i+1:]):
                    counter += 1
                    break
    print(counter)

if __name__ == "__main__":
    main()