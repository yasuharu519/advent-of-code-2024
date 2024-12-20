# coding: utf-8
import sys
from collections import defaultdict

def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    forward = defaultdict(set)
    backward = defaultdict(set)

    result = 0

    for line in lines:
        if "|" in line:
            a, b = line.split("|")
            forward[a].add(b)
            backward[b].add(a)
        elif line.strip() == "":
            continue
        else:
            nums = line.split(",")
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
            if flag:
                result += int(nums[len(nums) // 2])
    print(result)

if __name__ == "__main__":
    main()