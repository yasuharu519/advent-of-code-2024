# coding: utf-8
from collections import deque

def main():
    line = input().strip()

    queue = deque()
    actualIndex = 0
    for i,c in enumerate(line):
        print(i, c)
        # num, index
        if i % 2 == 0:
            # file
            queue.append((int(c), i // 2, actualIndex, True))
        else:
            queue.append((int(c), i // 2, actualIndex, False))
        actualIndex += int(c)

    if queue[-1][2] == False:
        queue.pop()

    result = 0
    while queue:
        num, file_index, index, isNum = queue.popleft()
        # 数字の場合
        if isNum:
            start, end = index, index + num - 1
            result += file_index * (start + end) * num // 2
            print(f"file_index: {file_index}, start: {start}, end: {end}, result: {result}")
        # space の場合
        else:
            rest = num
            while queue and rest > 0:
                while queue[-1][3] == False:
                    queue.pop()
                if not queue:
                    break
                lastNum, lastFileIndex, lastIndex, _ = queue.pop()
                if rest >= lastNum:
                    start, end = index, index + lastNum - 1
                    result += lastFileIndex * (start + end) * lastNum // 2
                    rest -= lastNum
                    index += lastNum
                    print(f"file_index: {lastFileIndex}, start: {start}, end: {end}, result: {result}")
                else:
                    start, end = index, index + rest - 1
                    result += lastFileIndex * (start + end) * rest // 2
                    queue.append((lastNum - rest, lastFileIndex, lastIndex, True))
                    rest = 0
                    print(f"file_index: {lastFileIndex}, start: {start}, end: {end}, result: {result}")
    print(result)

if __name__ == "__main__":
    main()