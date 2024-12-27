import os
import re
from typing import List, Tuple


def find_multiplications(value: str) -> List[Tuple[int, int]]:
    mul_pattern: re.Pattern[str] = re.compile(r"mul\((\d+),(\d+)\)")
    return [(int(t[0]), int(t[1])) for t in mul_pattern.findall(value)]


def get_sum(value: str) -> int:
    return sum(t[0] * t[1] for t in find_multiplications(value))


def part_1() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day03.txt")) as f:
        ret = get_sum(f.read())
        print(ret)


def find_multiplications_do_dont(value: str) -> List[Tuple[int, int]]:
    mul_do_pattern: re.Pattern[str] = re.compile(
        r"(do\(\))|(don't\(\))|(?:mul\((\d+),(\d+)\))"
    )
    generate = True
    ret: List[Tuple[int, int]] = []
    for m in mul_do_pattern.finditer(value):
        if m.group() == "do()":
            generate = True
        elif m.group() == "don't()":
            generate = False
        elif generate:
            ret.append((int(m.group(3)), int(m.group(4))))
    return ret


def get_sum_do_dont(value: str) -> int:
    return sum(t[0] * t[1] for t in find_multiplications_do_dont(value))


def part_2() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../data/day03.txt")) as f:
        ret = get_sum_do_dont(f.read())
        print(ret)


if __name__ == "__main__":
    part_2()
