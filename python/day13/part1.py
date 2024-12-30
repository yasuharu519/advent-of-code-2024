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