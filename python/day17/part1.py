import sys

def main():
    lines = [line.strip() for line in sys.stdin.readlines()]

    A = int(lines[0][12:])
    B = int(lines[1][12:])
    C = int(lines[2][12:])

    programs = list(map(int, lines[4][9:].strip().split(",")))
    n = len(programs)

    def get_combo_value(combo) -> int:
        if 0 <= combo <= 3:
            return combo
        elif combo == 4:
            return A
        elif combo == 5:
            return B
        elif combo == 6:
            return C
        else:
            raise ValueError("Invalid combo value")

    print(f"Initial values: {A}, {B}, {C}")
    counter = 0
    result = []
    while counter < n:
        print(f"Program: {programs[counter]}, combo: {programs[counter + 1]}")
        program = programs[counter]
        if program == 0:
            counter += 1
            combo = get_combo_value(programs[counter])
            counter += 1
            A = A // (1 << combo)
        elif program == 1:
            counter += 1
            combo = programs[counter]
            counter += 1
            B = B ^ combo
        elif program == 2:
            counter += 1
            combo = get_combo_value(programs[counter])
            counter += 1
            B = combo % 8
        elif program == 3:
            if A == 0:
                counter += 2
                continue
            else:
                counter += 1
                combo = programs[counter]
                counter = combo
        elif program == 4:
            counter += 1
            counter += 1
            B = B ^ C
        elif program == 5:
            counter += 1
            combo = get_combo_value(programs[counter])
            counter += 1
            result.append(combo % 8)
        elif program == 6:
            counter += 1
            combo = get_combo_value(programs[counter])
            counter += 1
            B = A // (1 << combo)
        elif program == 7:
            counter += 1
            combo = get_combo_value(programs[counter])
            counter += 1
            C = A // (1 << combo)
        print(f"Values: {A}, {B}, {C}")
    print(",".join(map(str, result)))


if __name__ == "__main__":
    main()