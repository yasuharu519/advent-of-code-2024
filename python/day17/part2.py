import sys
from typing import List

def calculation(currentA: int, rest: List[int], path: List[int]) -> List[int]:
    if not rest:
        print(currentA)
        return path
    
    currentA <<= 3
    for origB in range(1 << 3):
        a = currentA + origB
        b = origB ^ 5
        c = a // (1 << b)
        b = b ^ 6
        b = b ^ c
        if (b % 8) == rest[0]:
            res = calculation(a, rest[1:], path + [origB])
            if res:
                return res
    return []

def main():
    lines = [line.strip() for line in sys.stdin.readlines()]

    A = int(lines[0][12:])
    B = int(lines[1][12:])
    C = int(lines[2][12:])

    programs = list(map(int, lines[4][9:].strip().split(",")))
    programs.reverse()

    print(calculation(0, programs, []))


if __name__ == "__main__":
    main()