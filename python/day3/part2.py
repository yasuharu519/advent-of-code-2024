# coding: utf-8
import sys
import re

pattern = re.compile(r"(mul)\((\d{1,3}),(\d{1,3})\)|(?:do|don't)\(\)")

def main():
    result = 0
    enabled = True
    for line in sys.stdin.readlines():
        line = line.strip()
        for match in pattern.finditer(line):
            if match.group(1) == "mul":
                if enabled:
                    result += int(match.group(2)) * int(match.group(3))
            elif match.group(0) == "do()":
                enabled = True
            else:
                enabled = False
    print(result)

if __name__ == "__main__":
    main()