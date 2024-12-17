# coding: utf-8

import sys

def main():
    lines = [x.strip() for x in sys.stdin.readlines()]

    def search(i: int, j: int) -> bool:
        indices = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        pairs = [
            ((0, 1), (2, 3)),
            ((0, 3), (1, 2)),
        ]

        for l, r in pairs:
            l1, l2 = l
            r1, r2 = r

            l1x, l1y = i + indices[l1][0], j + indices[l1][1]
            l2x, l2y = i + indices[l2][0], j + indices[l2][1]
            r1x, r1y = i + indices[r1][0], j + indices[r1][1]
            r2x, r2y = i + indices[r2][0], j + indices[r2][1]

            if lines[l1x][l1y] == "M" and \
                lines[l2x][l2y] == "M" and \
                lines[r1x][r1y] == "S" and \
                lines[r2x][r2y] == "S":
                return True
            elif lines[l1x][l1y] == "S" and \
                lines[l2x][l2y] == "S" and \
                lines[r1x][r1y] == "M" and \
                lines[r2x][r2y] == "M":
                return True
        return False
    
    result = 0
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            if lines[i][j] == "A":
                result += int(search(i, j))
    print(result)


if __name__ == "__main__":
    main()