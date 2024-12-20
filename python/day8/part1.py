# coding: utf-8
import sys
from collections import defaultdict

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
        for i in range(len(anntennas)):
            for j in range(len(anntennas)):
                if i != j:
                    vec = (anntennas[j][0] - anntennas[i][0], anntennas[j][1] - anntennas[i][1])
                    antivec = (-vec[0], -vec[1])
                    p = anntennas[i][0] + antivec[0], anntennas[i][1] + antivec[1]
                    if 0 <= p[0] < m and 0 <= p[1] < n:
                        antinodes.add(p)
    print(len(antinodes))


if __name__ == "__main__":
    main()