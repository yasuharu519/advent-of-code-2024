# coding: utf-8
import sys
import re

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

def main():
    result = 0
    for line in sys.stdin.readlines():
        line = line.strip()
        for d1, d2 in pattern.findall(line):
            result += int(d1) * int(d2)
    print(result)

if __name__ == "__main__":
    main()