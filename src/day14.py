import os
import re
from typing import NamedTuple


class Grid(NamedTuple):
    w: int
    h: int


class Robot:
    def __init__(self, x: int, y: int, vx: int, vy: int):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def move(self, grid: Grid) -> None:
        self.x = (self.x + self.vx) % grid.w
        self.y = (self.y + self.vy) % grid.h


def parse_input(s: str) -> list[Robot]:
    return [
        Robot(*map(int, re.findall(r"-?\d+", line))) for line in s.strip().splitlines()
    ]


def robots_by_quadrants(robots: list[Robot], grid: Grid) -> list[int]:
    left = grid.w // 2
    top = grid.h // 2

    first, second, third, fourth = 0, 0, 0, 0
    for rbt in robots:
        if rbt.x < left and rbt.y < top:
            first += 1
        elif rbt.x > left and rbt.y < top:
            second += 1
        elif rbt.x < left and rbt.y > top:
            third += 1
        elif rbt.x > left and rbt.y > top:
            fourth += 1

    return [first, second, third, fourth]


def get_safety_factor(s: str, w: int, h: int, t: int) -> int:
    robots = parse_input(s)
    grid = Grid(w, h)
    for _ in range(t):
        for rbt in robots:
            rbt.move(grid)
    r = robots_by_quadrants(robots, grid)
    return r[0] * r[1] * r[2] * r[3]


def print_grid(robots: list[Robot], grid: Grid) -> None:
    for y in range(grid.h):
        for x in range(grid.w):
            for rbt in robots:
                if rbt.x == x and rbt.y == y:
                    print("X", end="")
                    break
            else:
                print(" ", end="")
        print()


def find_easter_egg(s: str, w: int, h: int) -> None:
    robots = parse_input(s)
    grid = Grid(w, h)

    cnt = 0

    while True:  # pylint: disable=too-many-nested-blocks
        maybe = True
        y = 0
        while y < grid.h and maybe:
            x = 0
            while x < grid.w and maybe:
                r = 0
                for rbt in robots:
                    if rbt.x == x and rbt.y == y:
                        r += 1
                        if r > 1:
                            maybe = False
                            break
                x += 1
            y += 1
        if maybe:
            print_grid(robots, grid)
            print(cnt)
            break
        cnt += 1
        for rbt in robots:
            rbt.move(grid)


def part1():
    with open(os.path.join(os.path.dirname(__file__), "day14.txt")) as f:
        print(get_safety_factor(f.read(), 101, 103, 100))


def part2():
    with open(os.path.join(os.path.dirname(__file__), "day14.txt")) as f:
        find_easter_egg(f.read(), 101, 103)


if __name__ == "__main__":
    part2()
