# coding: utf-8
from collections import deque

def main():
    line = input().strip()

    queue = deque()
    pos = 0
    for i, c in enumerate(line):
        c = int(c)
        if i % 2 == 0:
            # isNum, num, file_index, pos
            queue.append((True, c, pos, i // 2))
        else:
            queue.append((False, c, pos))
        pos += int(c)

    if queue[-1][2] == False:
        queue.pop()

    result = 0
    while queue:
        file_data = queue.popleft()
        is_num, rest = file_data[0], file_data[1:]
        # 数字の場合
        if is_num:
            num, pos, file_index = rest
            start, end = pos, pos + num - 1
            result += file_index * (start + end) * num // 2
            print(f"file_index: {file_index}, start: {start}, end: {end}, result: {result}")
        # space の場合
        else:
            num, pos = rest
            # 末尾が space の場合は削除
            while queue and queue[-1][0] == False:
                queue.pop()
            if not queue:
                break
            # 末尾から数字のものを取り出す
            _, last_num, _last_pos, file_index = queue.pop()
            if num >= last_num:
                taken_num = last_num
                # スペースを先頭に追加
                queue.appendleft((False, num - taken_num, pos + taken_num))
            else:
                taken_num = num
                # 残りの数を末尾に追加
                queue.append((True, last_num - taken_num, pos + taken_num, file_index))
            start, end = pos, pos + taken_num - 1
            result += file_index * (start + end) * taken_num // 2
            print(f"file_index: {file_index}, start: {start}, end: {end}, result: {result}")
    print(result)

if __name__ == "__main__":
    main()