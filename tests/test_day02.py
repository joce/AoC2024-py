from day02 import get_safe_lines_count, get_safe_lines_count_damper


def test_part1():
    values = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]
    assert get_safe_lines_count(values) == 2


def test_part2():
    values = [
        "7 6 4 2 1",  # Safe
        "1 2 7 8 9",  # Unsafe
        "9 7 6 2 1",  # Unsafe
        "1 3 2 4 5",  # Safe by removing second level, 3
        "8 6 4 4 1",  # Safe by removing third level, 4
        "1 3 6 7 9",  # Safe
        "1 3 6 9 1",  # Safe by removing last level, 1
        "1 6 7 8 9",  # Safe by removing first level, 1
        "1 1 2 3 4",  # Safe by removing first level, 1
    ]
    assert get_safe_lines_count_damper(values) == 7
