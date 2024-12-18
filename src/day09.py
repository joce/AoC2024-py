from helper import apply_lines_from_file


def generate_layout(s: str) -> list[int]:
    _id = 0
    res: list[int] = []
    for i, a in enumerate([int(c) for c in s]):
        if i % 2 == 0:
            res.extend([_id] * a)
            _id += 1
        else:
            res.extend([-1] * a)
    return res


def compact_layout(layout: list[int]) -> list[int]:
    left = 0
    right = len(layout) - 1
    while left <= right:
        if layout[left] != -1:
            left += 1
            continue

        if layout[right] == -1:
            right -= 1
            continue

        if left > right:
            break
        layout[left] = layout[right]
        layout[right] = -1
    return layout


def checksum_layout(layout: list[int]) -> int:
    return sum(i * c for i, c in enumerate(layout) if c >= 0)


def process_layout(inp: list[str]) -> int:
    layout = generate_layout(inp[0])
    layout = compact_layout(layout)
    total = checksum_layout(layout)
    return total


def part1() -> None:
    apply_lines_from_file("day09.txt", process_layout)


if __name__ == "__main__":
    part1()
