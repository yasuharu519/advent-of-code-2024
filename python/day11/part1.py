# coding: utf-8
from functools import cache

def main():
    nums = list(map(int, input().split()))

    @cache
    def count(v: int, rest: int) -> int:
        if rest == 0:
            return 1
        
        str_num = str(v)
        str_length = len(str_num)
        if v == 0:
            return count(1, rest-1)
        elif str_length % 2 == 0:
            left, right = str_num[:str_length//2], str_num[str_length//2:]
            return count(int(left), rest-1) + count(int(right), rest-1)
        else:
            return count(v * 2024, rest-1)
    
    result = 0
    for v in nums:
        result += count(v, 25)
    print(result)


if __name__ == "__main__":
    main()