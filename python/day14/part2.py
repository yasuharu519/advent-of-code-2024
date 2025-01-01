import os
import time
import sys

MAP_W = 101
MAP_H = 103

RED = "\033[31m"
RESET = "\033[0m"

def print_robots_positions(robots):
    map_to_display = [['.'] * MAP_W for _ in range(MAP_H)]

    for px, py, _, _ in robots:
        map_to_display[py][px] = f"{RED}O{RESET}"
    
    for row in map_to_display:
        print("".join(row))

def main():
    lines = [line.strip() for line in sys.stdin.readlines()]
    robots = []
    for line in lines:
        pos, vec = line.strip().split(" ")
        pos, vec = pos[2:], vec[2:]
        px, py = map(int, pos.split(","))
        vx, vy = map(int, vec.split(","))
        robots.append((px, py, vx, vy))
    
    # 33, 87, 134, 190, 235, 293... の時にパターンが見える
    t = 33
    while t <= 7709:
        time.sleep(0.1)
        os.system("clear")
        print(f"Second {t}")

        robots_t = []

        for px, py, vx, vy in robots:
            nx, ny = px + vx * t, py + vy * t
            nx, ny = nx % MAP_W, ny % MAP_H
            robots_t.append((nx, ny, vx, vy))
        print_robots_positions(robots_t)
        t += 101
        print()


if __name__ == "__main__":
    main()