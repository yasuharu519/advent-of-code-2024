import sys

def main():
    chunks = sys.stdin.read().split("\n\n")
    result = 0

    for chunk in chunks:
        lines = chunk.strip().split("\n")
        button_a, button_b, prize = lines
        button_a = button_a.removeprefix("Button A:")
        button_b = button_b.removeprefix("Button B: ")
        prize = prize.removeprefix("Prize: ")

        ax, ay = map(int, [x[2:] for x in button_a.strip().split(", ")])
        bx, by = map(int, [x[2:] for x in button_b.strip().split(", ")])
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