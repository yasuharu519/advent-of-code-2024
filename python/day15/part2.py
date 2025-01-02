# coding: utf-8
from collections import deque
from typing import Tuple
import os
import sys

move_vector = {
    "<": (0, -1),
    ">": (0, +1),
    "^": (-1, 0),
    "v": (1, 0)
}

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

    # 対象のブロックを動かせるかどうか
    def can_move(px, py, vx, vy):
        nx, ny = px + vx, py + vy
        if S[px][py] == "[":
            if S[nx][ny] == "." and S[nx][ny+1] == ".":
                return True
            elif S[nx][ny] == "#" or S[nx][ny+1] == "#":
                return False
            elif S[nx][ny] == "." and S[nx][ny+1] == "[":
                return can_move(nx, ny+1, vx, vy)
            elif S[nx][ny] == "]" and S[nx][ny+1] == ".":
                return can_move(nx, ny, vx, vy)
            elif S[nx][ny] == "[" and S[nx][ny+1] == "]":
                return can_move(nx, ny, vx, vy)
            elif S[nx][ny] == "]" and S[nx][ny+1] == "[":
                return can_move(nx, ny, vx, vy) and can_move(nx, ny+1, vx, vy)
        elif S[px][py] == "]":
            if S[nx][ny-1] == "." and S[nx][ny] == ".":
                return True
            elif S[nx][ny-1] == "#" or S[nx][ny] == "#":
                return False
            elif S[nx][ny-1] == "]" and S[nx][ny] == ".":
                return can_move(nx, ny-1, vx, vy)
            elif S[nx][ny-1] == "." and S[nx][ny] == "[":
                return can_move(nx, ny, vx, vy)
            elif S[nx][ny-1] == "[" and S[nx][ny] == "]":
                return can_move(nx, ny, vx, vy)
            elif S[nx][ny-1] == "]" and S[nx][ny] == "[":
                return can_move(nx, ny-1, vx, vy) and can_move(nx, ny, vx, vy)

    # 移動
    def move_left(p, v) -> Tuple:
        # 現在の位置
        px, py = p
        # 移動量
        dx, dy = v

        # 左のものを確認
        nx, ny = px, py + dy
        hasBlock = False
        while S[nx][ny] == "[" or S[nx][ny] == "]":
            hasBlock = True
            ny += dy
        if S[nx][ny] == ".":
            if hasBlock:
                yy = ny
                while yy != py + dy:
                    S[nx][yy] = S[nx][yy+1]
                    yy -= dy
                S[px][py+dy] = "."
            S[px][py] = "."
            S[px][py+dy] = "@"
            return (px, py+dy)
        else:
            return (px, py)

    def move_right(p, v):
        # 現在の位置
        px, py = p
        # 移動量
        dx, dy = v

        # 右のものを確認
        nx, ny = px, py + 1
        hasBlock = False
        while S[nx][ny] == "[" or S[nx][ny] == "]":
            hasBlock = True
            ny += 1
        if S[nx][ny] == ".":
            if hasBlock:
                yy = ny
                while yy != py + 1:
                    S[nx][yy] = S[nx][yy-1]
                    yy -= 1
                S[px][py+1] = "."
            S[px][py] = "."
            S[px][py+1] = "@"
            return (px, py + 1)
        else:
            return (px, py)

    def move_up(p, v):
        # 現在の位置
        px, py = p
        # 移動量
        dx, dy = v

        # 上のものを確認
        nx, ny = px - 1, py
        if S[nx][ny] == ".":
            S[nx][ny] = "@"
            S[px][py] = "."
            return (px - 1, py)
        elif S[nx][ny] == "#":
            return (px, py)

        if not can_move(nx, ny, -1, 0):
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
                queue.append((x-1, y))
            elif S[x][y] == "]":
                queue.append((x, y-1))
                queue.append((x-1, y))
        
        for x, y in sorted(list(cells)):
            S[x-1][y] = S[x][y]
            S[x][y] = "."
        S[px-1][py] = S[px][py]
        S[px][py] = "."
        return (px - 1, py)


    def move_down(p, v):
        # 現在の位置
        px, py = p
        # 移動量
        dx, dy = v

        # 下のものを確認
        nx, ny = px + 1, py
        if S[nx][ny] == ".":
            S[nx][ny] = "@"
            S[px][py] = "."
            return (px + 1, py)
        elif S[nx][ny] == "#":
            return (px, py)

        if not can_move(nx, ny, 1, 0):
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
                queue.append((x+1, y))
            elif S[x][y] == "]":
                queue.append((x, y-1))
                queue.append((x+1, y))
        
        for x, y in sorted(list(cells), reverse=True):
            S[x+1][y] = S[x][y]
            S[x][y] = "."
        S[px+1][py] = S[px][py]
        S[px][py] = "."
        return (px + 1, py)
    
    # 移動
    i = 0
    x, y = current
    for move_line in moves:
        for move in move_line:
            os.system("clear")
            print(f"Move: {move}")
            if move == "<":
                current = move_left(current, move_vector[move])
            elif move == ">":
                current = move_right(current, move_vector[move])
            elif move == "^":
                current = move_up(current, move_vector[move])
            else:
                current = move_down(current, move_vector[move])
            # print result
            for line in S:
                print("".join(line))
            i += 1

    result = 0
    for i in range(m):
        for j in range(n):
            if S[i][j] == "[":
                result += 100 * i + j
    for line in S:
        print("".join(line))
    print(result)



if __name__ == "__main__":
    main()