from helper import apply_lines_from_file


def is_line_safe(line: str) -> bool:
    vals = [int(v) for v in line.split(" ")]
    if vals[0] == vals[1]:  # Handle equal values case first
        return False

    # direction will be 1 for increasing, -1 for decreasing
    direction = 1 if vals[0] < vals[1] else -1

    for i in range(len(vals) - 1):
        diff = (vals[i + 1] - vals[i]) * direction
        if diff <= 0 or diff > 3:
            return False
    return True


def is_line_safe_damper(line: str) -> bool:
    if is_line_safe(line):
        return True
    vals = line.split(" ")
    for i in range(len(vals)):
        if is_line_safe(" ".join(vals[:i] + vals[i + 1 :])):
            return True
    return False


def get_safe_lines_count(lines: list[str]) -> int:
    return sum(is_line_safe(line) for line in lines)


def get_safe_lines_count_damper(lines: list[str]) -> int:
    return sum(is_line_safe_damper(line) for line in lines)


def part_1() -> None:
    apply_lines_from_file("day02.txt", get_safe_lines_count)


def part_2() -> None:
    apply_lines_from_file("day02.txt", get_safe_lines_count_damper)
