# coding: utf-8
from collections import deque

def main():
    line = input().strip()

    actualIndex = 0
    nums = deque()
    spaces = []
    for i,c in enumerate(line):
        num = int(c)
        # num, index
        if i % 2 == 0:
            # file
            nums.append((num, actualIndex, i // 2))
        else:
            spaces.append((num, actualIndex, i // 2))
        actualIndex += int(c)

    result = 0
    while nums:
        num, index, file_index = nums.pop()
        # print(f"num: {num}, index: {index}, file_index: {file_index}")
        # print(f"space: {spaces}")
        # num 以上の space を探す

        # space_index = bisect.bisect_left(spaces, (num, -1, 0))
        # while space_index < len(spaces) and spaces[space_index][1] >= index:
        #     spaces.pop(space_index)

        space_index = 0
        while space_index < len(spaces):
            space = spaces[space_index]
            if space[0] >= num and space[1] <= index:
                spaces.pop(space_index)
                start, end = space[1], space[1] + num - 1
                result += file_index * (start + end) * num // 2

                if space[0] > num:
                    spaces.insert(space_index, (space[0] - num, space[1] + num, space[2]))
                break
            space_index += 1

        # # 見つからなかった場合
        if space_index == len(spaces):
            start, end = index, index + num - 1
            result += file_index * (start + end) * num // 2
            print(f"file_index: {file_index}, start: {start}, end: {end}, result: {result}")
        # else:
    print(result)


if __name__ == "__main__":
    main()