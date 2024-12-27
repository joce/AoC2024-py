import re

from helper import apply_lines_from_file


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


def part_1() -> None:
    apply_lines_from_file("../data/day01.txt", find_distance_from_string_list)


def part_2() -> None:
    apply_lines_from_file("../data/day01.txt", compute_similarity_score)


if __name__ == "__main__":
    part_2()
