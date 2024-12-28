# coding: utf-8
from collections import deque

def main():
    line = input().strip()

    files = deque()
    spaces = []
    pos = 0
    for i,c in enumerate(line):
        num = int(c)
        if i % 2 == 0:
            files.append((num, pos, i // 2))
        else:
            spaces.append((num, pos, i // 2))
        pos += int(c)

    result = 0
    while files:
        num, index, pos = files.pop()
        space_index = 0
        while space_index < len(spaces):
            space = spaces[space_index]
            if space[0] >= num and space[1] <= index:
                spaces.pop(space_index)
                start, end = space[1], space[1] + num - 1
                result += pos * (start + end) * num // 2

                if space[0] > num:
                    spaces.insert(space_index, (space[0] - num, space[1] + num, space[2]))
                break
            space_index += 1
        else:
            start, end = index, index + num - 1
            result += pos * (start + end) * num // 2
            print(f"pos: {pos}, start: {start}, end: {end}, result: {result}")
    print(result)


if __name__ == "__main__":
    main()