# coding: utf-8
import sys
from typing import Tuple

def main():
    lines = [line.strip() for line in sys.stdin.readlines()]
    S = []
    moves = []
    input_map = True
    for line in lines:
        if line.strip() == "":
            input_map = False
        elif input_map:
            S.append(list(line))
        else:
            moves.append(line)

    # 場所の確認
    current = (0, 0)
    m = len(S)
    n = len(S[0])
    for i in range(m):
        for j in range(n):
            if S[i][j] == "@":
                current = (i, j)

    # 移動
    def move_left(px, py) -> Tuple:
        # 左のものを確認
        nx, ny = px, py - 1
        hasBlock = False
        while S[nx][ny] == "O":
            hasBlock = True
            ny -= 1
        if S[nx][ny] == ".":
            if hasBlock:
                S[nx][ny] = "O"
                S[px][py-1] = "."
            S[px][py] = "."
            S[px][py-1] = "@"
            return (px, py-1)
        else:
            return (px, py)
    def move_right(px, py):
        # 右のものを確認
        nx, ny = px, py + 1
        hasBlock = False
        while S[nx][ny] == "O":
            hasBlock = True
            ny += 1
        if S[nx][ny] == ".":
            if hasBlock:
                S[nx][ny] = "O"
                S[px][py+1] = "."
            S[px][py] = "."
            S[px][py+1] = "@"
            return (px, py + 1)
        else:
            return (px, py)
    def move_up(px, py):
        # 上のものを確認
        nx, ny = px - 1, py
        hasBlock = False
        while S[nx][ny] == "O":
            hasBlock = True
            nx -= 1
        if S[nx][ny] == ".":
            if hasBlock:
                S[nx][ny] = "O"
                S[px-1][py] = "."
            S[px][py] = "."
            S[px-1][py] = "@"
            return (px - 1, py)
        else:
            return (px, py)
    def move_down(px, py):
        # 下のものを確認
        nx, ny = px + 1, py
        hasBlock = False
        while S[nx][ny] == "O":
            hasBlock = True
            nx += 1
        if S[nx][ny] == ".":
            if hasBlock:
                S[nx][ny] = "O"
                S[px+1][py] = "."
            S[px][py] = "."
            S[px+1][py] = "@"
            return (px+1, py)
        else:
            return (px, py)
    
    # 移動
    x, y = current
    for move_line in moves:
        for move in move_line:
            if move == "<":
                x, y = move_left(x, y)
            elif move == ">":
                x, y = move_right(x, y)
            elif move == "^":
                x, y = move_up(x, y)
            else:
                x, y = move_down(x, y)
            # print result
            for line in S:
                print("".join(line))
    result = 0
    for i in range(m):
        for j in range(n):
            if S[i][j] == "O":
                result += 100 * i + j
    for line in S:
        print("".join(line))
    print(result)



if __name__ == "__main__":
    main()