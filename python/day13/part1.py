# coding: utf-8
import sys

def main():
    lines = [line.strip() for line in sys.stdin.readlines()]
    length = len(lines)
    problems = length // 4
    result = 0

    for problem_num in range(problems):
        button_a = lines[problem_num * 4 + 0][9:]
        # button_a.removeprefix("Button A:")
        ax, ay = map(int, [x[2:] for x in button_a.strip().split(", ")])
        button_b = lines[problem_num * 4 + 1][9:]
        # button_b.removeprefix("Button B: ")
        bx, by = map(int, [x[2:] for x in button_b.strip().split(", ")])
        prize = lines[problem_num * 4 + 2][7:]
        px, py = map(int, [x[2:] for x in prize.strip().split(", ")])

        cost = float('inf')

        for push_a in range(101):
            for push_b in range(101):
                x = ax * push_a + bx * push_b
                y = ay * push_a + by * push_b
                if x == px and y == py:
                    cost = min(cost, push_a * 3 + push_b)
        if cost != float('inf'):
            result += cost
    print(result)



if __name__ == "__main__":
    main()