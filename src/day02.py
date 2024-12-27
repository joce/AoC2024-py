from helper import apply_lines_from_file


def is_line_safe(vals: list[int]) -> bool:
    if vals[0] == vals[1]:  # Handle equal values case first
        return False

    # direction will be 1 for increasing, -1 for decreasing
    direction = 1 if vals[0] < vals[1] else -1

    for i in range(len(vals) - 1):
        diff = (vals[i + 1] - vals[i]) * direction
        if diff <= 0 or diff > 3:
            return False
    return True


def is_line_safe_damper(vals: list[int]) -> bool:
    if is_line_safe(vals):
        return True
    for i in range(len(vals)):
        if is_line_safe(vals[:i] + vals[i + 1 :]):
            return True
    return False


def get_safe_lines_count(lines: list[str]) -> int:
    return sum(is_line_safe([int(v) for v in line.split(" ")]) for line in lines)


def get_safe_lines_count_damper(lines: list[str]) -> int:
    return sum(is_line_safe_damper([int(v) for v in line.split(" ")]) for line in lines)


def part_1() -> None:
    apply_lines_from_file("../data/day02.txt", get_safe_lines_count)


def part_2() -> None:
    apply_lines_from_file("../data/day02.txt", get_safe_lines_count_damper)


if __name__ == "__main__":
    part_2()
