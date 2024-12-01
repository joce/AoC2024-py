import os
import os.path
import re
from typing import Callable


def find_distance_from_string_list(values: list[str]) -> int:
    list1, list2 = extract_data(values)

    return sum(abs(x - y) for x, y in zip(list1, list2))


def compute_similarity_score(values: list[str]) -> int:
    list1, list2 = extract_data(values)
    return sum(a * list2.count(a) for a in list1)


def extract_data(values: list[str]) -> tuple[list[int], list[int]]:
    pattern: re.Pattern[str] = re.compile(r"(\d+)   (\d+)")
    list1: list[int] = []
    list2: list[int] = []

    for inp in values:
        pair: tuple[str, str] = pattern.findall(inp)[0]
        list1.append(int(pair[0]))
        list2.append(int(pair[1]))
    # sort the lists
    list1.sort()
    list2.sort()
    return list1, list2


def apply_from_file(filename: str, func: Callable[[list[str]], int]) -> None:
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        lines: list[str] = f.readlines()
        ret: int = func(lines)
        print(ret)


def part_1() -> None:
    apply_from_file("day01.txt", find_distance_from_string_list)


def part_2() -> None:
    apply_from_file("day01.txt", compute_similarity_score)


if __name__ == "__main__":
    part_2()
