# coding: utf-8
from collections import deque
from typing import Tuple
import os
import sys
import time

move_vector = {
    "<": (0, -1),
    ">": (0, +1),
    "^": (-1, 0),
    "v": (1, 0)
}

RED = "\033[31m"
RESET = "\033[0m"

def print_positions(S):
    for line in S:
        for c in line:
            if c == "@":
                print(f"{RED}{c}{RESET}", end="")
            else:
                print(c, end="")
        print()

# 対象のブロックを動かせるかどうか
def can_move(S, p, v) -> bool:
    px, py = p
    dx, dy = v

    pushing_left_side = (S[px][py] == "[")
    if pushing_left_side:
        px_l, py_l = px, py
        px_r, py_r = px, py + 1
    else:
        px_l, py_l = px, py - 1
        px_r, py_r = px, py
    
    nx_l, ny_l = px_l + dx, py_l + dy
    nx_r, ny_r = px_r + dx, py_r + dy

    if S[nx_l][ny_l] == "#" or S[nx_r][ny_r] == "#":
        return False
    if S[nx_l][ny_l] == "." and S[nx_r][ny_r] == ".":
        return True

    res = []
    for (xx, yy) in [(nx_l, ny_l), (nx_r, ny_r)]:
        if S[xx][yy] in ["[", "]"]:
            res.append(can_move(S, (xx, yy), v))
        elif S[xx][yy] == ".":
            res.append(True)
        else:
            res.append(False)
    return all(res)

def main():
    chunks = sys.stdin.read().split("\n\n")
    map_data, move_data = chunks

    moves = "".join(move_data.split("\n"))
    S = []
    for line in map_data.split("\n"):
        new_line = []
        for c in line:
            if c == "#":
                new_line.append("#")
                new_line.append("#")
            elif c == "O":
                new_line.append("[")
                new_line.append("]")
            elif c == ".":
                new_line.append(".")
                new_line.append(".")
            elif c == "@":
                new_line.append("@")
                new_line.append(".")
        S.append(new_line)

    print("Initial")
    for line in S:
        print("".join(line))

    # 場所の確認
    current = (0, 0)
    m = len(S)
    n = len(S[0])
    print(f"m: {m}, n: {n}")
    for i in range(m):
        for j in range(n):
            if S[i][j] == "@":
                current = (i, j)

    # 移動
    def move_horizontal(p, v) -> Tuple:
        # 現在の位置
        px, py = p
        # 移動量
        _, dy = v

        nx, ny = px, py + dy
        # 移動先にブロックがない場合
        if S[nx][ny] == ".":
            S[nx][ny], S[px][py] = "@", "."
            return (nx, ny)
        # 移動先が障害物の場合
        elif S[nx][ny] == "#":
            return (px, py)

        while S[nx][ny] == "[" or S[nx][ny] == "]":
            ny += dy
            if S[nx][ny] == ".":
                break
            elif S[nx][ny] == "#":
                return (px, py)

        # ブロックを奥から順に動かす
        yy = ny
        while yy != py + dy:
            S[nx][yy] = S[nx][yy-dy]
            yy -= dy
        S[px][py] = "."
        return (px, py+dy)

    def move_vertical(p, v):
        # 現在の位置
        px, py = p
        # 移動量
        dx, _ = v

        nx, ny = px + dx, py
        # 移動先にブロックがない場合
        if S[nx][ny] == ".":
            S[nx][ny], S[px][py] = "@", "."
            return (nx, ny)
        # 移動先が障害物の場合
        elif S[nx][ny] == "#":
            return (px, py)
        # 障害物を押せるかどうか
        if not can_move(S, (nx, ny), v):
            return (px, py)
        
        queue = deque([(nx, ny)])
        cells = set()
        while queue:
            x, y = queue.popleft()
            if (x, y) in cells:
                continue
            if S[x][y] == "." or S[x][y] == "#":
                continue
            cells.add((x, y))
            if S[x][y] == "[":
                queue.append((x, y+1))
                queue.append((x+dx, y))
            elif S[x][y] == "]":
                queue.append((x, y-1))
                queue.append((x+dx, y))
        
        sort_reverse = (dx > 0)
        for x, y in sorted(list(cells), reverse=sort_reverse):
            S[x+dx][y] = S[x][y]
            S[x][y] = "."
        S[px+dx][py] = S[px][py]
        S[px][py] = "."
        return (px + dx, py)
    
    # 移動
    i = 0
    x, y = current
    for move_line in moves:
        for move in move_line:
            os.system("clear")
            
            print(f"Move: {move}")
            if move == "<" or move == ">":
                current = move_horizontal(current, move_vector[move])
            else:
                current = move_vertical(current, move_vector[move])
            print_positions(S)
            # time.sleep(0.1)
            i += 1

    result = 0
    for i in range(m):
        for j in range(n):
            if S[i][j] == "[":
                result += 100 * i + j
    print(result)



if __name__ == "__main__":
    main()