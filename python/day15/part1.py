# coding: utf-8
import sys
from typing import Tuple

move_vector = {
    "<": (0, -1),
    ">": (0, +1),
    "^": (-1, 0),
    "v": (1, 0)
}

def main():
    chunks = sys.stdin.read().split("\n\n")
    map_data, move_data = chunks

    # 入力データの整形
    S = [list(line.strip()) for line in map_data.split("\n")]
    moves = "".join(move_data.split("\n"))

    # 場所の確認
    current = (0, 0)
    m = len(S)
    n = len(S[0])
    for i in range(m):
        for j in range(n):
            if S[i][j] == "@":
                current = (i, j)

    # 移動
    def move_robot(p, v) -> Tuple:
        # 現在の位置
        px, py = p
        # 移動量
        dx, dy = v
        # 左のものを確認
        nx, ny = px + dx, py + dy
        hasBlock = False
        while S[nx][ny] == "O":
            hasBlock = True
            nx, ny = nx + dx, ny + dy
        if S[nx][ny] == ".":
            if hasBlock:
                S[nx][ny] = "O"
                S[px+dx][py+dy] = "."
            S[px][py] = "."
            S[px+dx][py+dy] = "@"
            return (px + dx, py + dy)
        else:
            return (px, py)
    
    # 移動
    for move in moves:
        current = move_robot(current, move_vector[move])
    result = 0
    for i in range(m):
        for j in range(n):
            if S[i][j] == "O":
                result += 100 * i + j

    # 最終的な結果を出力
    for line in S:
        print("".join(line))
    print(result)



if __name__ == "__main__":
    main()