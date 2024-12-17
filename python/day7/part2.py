# coding: utf-8

import sys

def main():
    lines = [x.strip() for x in sys.stdin.readlines()]

    def search(nums, current, target, path) -> bool:
        if current > target:
            return False
        if not nums:
            if current == target:
                print(f"{target} = {path}")
                return True
            else:
                return False
        l = len(str(nums[0]))
        res = False
        res |= search(nums[1:], current + nums[0], target, path + " + {}".format(nums[0]))
        res |= search(nums[1:], current * nums[0], target, path + " * {}".format(nums[0]))
        res |= search(nums[1:], (current * (10 ** l)) + nums[0], target, path + " || {}".format(nums[0]))
        return res
    
    result = 0
    for line in lines:
        target, rest = line.split(":")
        target = int(target)
        nums = [int(x) for x in rest.strip().split()]
        if search(nums[1:], nums[0], target, "{}".format(nums[0])):
            result += target
    print(result)


if __name__ == "__main__":
    main()