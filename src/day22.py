import os
from typing import TypeAlias


def mix(a: int, b: int) -> int:
    return a ^ b


def prune(a: int) -> int:
    return a % 16777216


def compute(secret: int) -> int:
    for factor in [64, 1 / 32, 2048]:
        secret = prune(mix(int(secret * factor), secret))
    return secret


def solve(secrets: list[int]) -> int:
    total = 0
    for secret in secrets:
        for _ in range(2000):
            secret = compute(secret)
        total += secret
    return total


def part1() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../data/day22.txt")) as f:
        print(solve([int(line) for line in f.readlines()]))


############### Part 2 ###############


Pattern: TypeAlias = tuple[int, int, int, int]


def get_last_digits(secret: int) -> list[int]:
    digits: list[int] = [0] * 2001
    digits[0] = secret % 10
    for i in range(1, 2001):
        secret = compute(secret)
        digits[i] = secret % 10
    return digits


def get_deltas(digits: list[int]) -> list[int]:
    deltas: list[int] = []
    prev = digits[0]
    for d in digits[1:]:
        deltas.append(d - prev)
        prev = d
    return deltas


def get_pattern_map(deltas: list[int], digits: list[int]) -> dict[Pattern, int]:
    patterns: dict[Pattern, int] = {}
    for i in range(len(deltas) - 3):  # -3 to ensure we have 4 deltas
        pattern: Pattern = tuple(deltas[i : i + 4])  # type: ignore
        if pattern not in patterns:  # only keep first occurrence
            patterns[pattern] = digits[i + 4]
    return patterns


def get_all_patterns(secrets: list[int]) -> dict[Pattern, list[int]]:
    res: dict[Pattern, list[int]] = {}
    for secret in secrets:
        digits = get_last_digits(secret)
        deltas = get_deltas(digits)
        pm = get_pattern_map(deltas, digits)
        for k, v in pm.items():
            if k in res:
                res[k].append(v)
            else:
                res[k] = [v]
    return res


def get_max_pattern(pat_dict: dict[Pattern, list[int]]) -> int:
    max_v = -1
    for v in pat_dict.values():
        val = sum(v)
        max_v = max(max_v, val)
    return max_v


def part2() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../data/day22.txt")) as f:
        pat_dict = get_all_patterns([int(line) for line in f.readlines()])
        max_v = get_max_pattern(pat_dict)
        print(max_v)


if __name__ == "__main__":
    part2()
