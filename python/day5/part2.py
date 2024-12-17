# coding: utf-8

import sys
from collections import defaultdict
from typing import List
from graphlib import TopologicalSorter

def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    forward = defaultdict(set)
    backward = defaultdict(set)

    result = 0

    def is_orderd(nums: List[str]) -> bool:
        num_with_index = dict([(x, i) for i, x in enumerate(nums)])
        flag = True
        for i, v in enumerate(nums):
            if v in forward:
                for x in forward[v]:
                    if x in num_with_index and num_with_index[x] < i:
                        flag = False
                        break
            if v in backward:
                for x in backward[v]:
                    if x in num_with_index and num_with_index[x] > i:
                        flag = False
                        break
        return flag
    

    line_count = 0
    for line in lines:
        line_count += 1
        if "|" in line:
            a, b = line.split("|")
            forward[a].add(b)
            backward[b].add(a)
        elif line.strip() == "":
            continue
        else:
            nums = line.split(",")
            nums_set = set(nums)
            if not is_orderd(nums):
                topo = TopologicalSorter()
                for v in nums:
                    predessors = [x for x in forward[v] if x in nums_set]
                    topo.add(v, *predessors)
                t = tuple(topo.static_order())
                result += int(t[len(t) // 2])
    print(result)

if __name__ == "__main__":
    main()