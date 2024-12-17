# coding: utf-8

import sys
from collections import defaultdict
from itertools import combinations

def main():
    lines = [list(x.strip()) for x in sys.stdin.readlines()]
    m = len(lines)
    n = len(lines[0])
    nodemap = defaultdict(list)

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != ".":
                nodemap[c].append((i, j))
    antinodes = set()

    for key, anntennas in nodemap.items():
        for pair in combinations(anntennas, 2):
            # 0 -> 1
            v1 = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
            # 1 -> 0
            v2 = (-v1[0], -v1[1])
            antinodes.add(pair[0])
            antinodes.add(pair[1])
            pn1 = (pair[1][0] + v1[0], pair[1][1] + v1[1])
            while 0 <= pn1[0] < m and 0 <= pn1[1] < n:
                antinodes.add(pn1)
                pn1 = (pn1[0] + v1[0], pn1[1] + v1[1])
            pn2 = (pair[0][0] + v2[0], pair[0][1] + v2[1])
            while 0 <= pn2[0] < m and 0 <= pn2[1] < n:
                antinodes.add(pn2)
                pn2 = (pn2[0] + v2[0], pn2[1] + v2[1])
    print(len(antinodes))


if __name__ == "__main__":
    main()