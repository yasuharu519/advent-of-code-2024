# coding: utf-8
import sys

def main():
    lines = [line.strip() for line in sys.stdin.readlines()]
    length = len(lines)
    problems = (length + 1) // 4
    result = 0

    for problem_num in range(problems):
        button_a = lines[problem_num * 4 + 0][9:]
        ax, ay = map(int, [x[2:] for x in button_a.strip().split(", ")])
        button_b = lines[problem_num * 4 + 1][9:]
        bx, by = map(int, [x[2:] for x in button_b.strip().split(", ")])
        prize = lines[problem_num * 4 + 2][7:]
        px, py = map(int, [x[2:] for x in prize.strip().split(", ")])
        px, py = px + 10000000000000, py + 10000000000000

        detA = ax * by - ay * bx

        detA_M = px * by - py * bx
        detA_N = ax * py - ay * px

        if detA != 0:
            m = detA_M // detA
            n = detA_N // detA
            if ax * m + bx * n == px and ay * m + by * n == py:
                print(ax, ay, bx, by, px, py, m, n, ax*m+bx*n, ay*m+by*n)
                result += 3 * m + n
    print(result)



if __name__ == "__main__":
    main()