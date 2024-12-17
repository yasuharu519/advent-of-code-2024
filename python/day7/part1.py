# coding: utf-8

import sys

def main():
    lines = [x.strip() for x in sys.stdin.readlines()]

    def search(nums, current, target) -> bool:
        if current == target:
            return True
        if current > target:
            return False
        if not nums:
            return False
        res = False
        res |= search(nums[1:], current + nums[0], target)
        res |= search(nums[1:], current * nums[0], target)
        return res
    
    result = 0
    for line in lines:
        target, rest = line.split(":")
        target = int(target)
        nums = [int(x) for x in rest.strip().split()]
        if search(nums[1:], nums[0], target):
            result += target
    print(result)


if __name__ == "__main__":
    main()