import os
import re
from dataclasses import dataclass

import numpy as np


@dataclass
class EqSystem:
    def __init__(self):
        self.a: tuple[int, int] = (0, 0)
        self.b: tuple[int, int] = (0, 0)
        self.p: tuple[int, int] = (0, 0)

    def __repr__(self):
        return f"A: {self.a}\nB: {self.b}\nP: {self.p}\n"

    def solve_integer(self) -> tuple[int, int] | tuple[None, None]:
        x = np.array([[self.a[0], self.b[0]], [self.a[1], self.b[1]]])
        y = np.array([self.p[0], self.p[1]])

        try:
            solution = np.linalg.solve(x, y)
            rounded = np.round(solution)
            if np.allclose(solution, rounded, rtol=1e-15, atol=1e-10):
                return (int(rounded[0]), int(rounded[1]))
            return (None, None)
        except np.linalg.LinAlgError:
            return (None, None)


INT_PATTERN = re.compile(r"\d+")


def parse_inp(data: str, special: bool = False) -> list[EqSystem]:
    lines = [line.strip() for line in data.splitlines()]
    eq_systems: list[EqSystem] = []
    i = 0
    while i < len(lines):
        s = EqSystem()
        s.a = tuple(int(s) for s in INT_PATTERN.findall(lines[i]))  # type: ignore
        s.b = tuple(int(s) for s in INT_PATTERN.findall(lines[i + 1]))  # type: ignore
        s.p = tuple(int(s) for s in INT_PATTERN.findall(lines[i + 2]))  # type: ignore
        if special:
            s.p = (s.p[0] + 10000000000000, s.p[1] + 10000000000000)
        eq_systems.append(s)
        i += 4
    return eq_systems


def find_cost(systems: list[EqSystem]) -> int:
    total = 0
    for s in systems:
        (n, m) = s.solve_integer()
        if n is not None and m is not None:
            total += 3 * n + m
    return total


def part1():
    with open(os.path.join(os.path.dirname(__file__), "../data/day13.txt")) as f:
        print(find_cost(parse_inp(f.read())))


def part2():
    with open(os.path.join(os.path.dirname(__file__), "../data/day13.txt")) as f:
        print(find_cost(parse_inp(f.read(), True)))


if __name__ == "__main__":
    part2()
