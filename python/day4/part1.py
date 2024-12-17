# coding: utf-8

import sys


def main():
    lines = [x.strip() for x in sys.stdin.readlines()]

    def search(i: int, j: int) -> int:
        count = 0
        directions = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0]

        for dx, dy in directions:
            x, y = i + dx, j + dy
            for c in "MAS":
                if 0 <= x < len(lines) and 0 <= y < len(lines[x]) and lines[x][y] == c:
                    x += dx
                    y += dy
                else:
                    break
            else:
                count += 1
        return count
    
    result = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "X":
                result += search(i, j)
    print(result)



if __name__ == "__main__":
    main()