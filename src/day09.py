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


def generate_layout2(s: str) -> tuple[list[int], dict[int, tuple[int, int]]]:
    """
    Returns:
        tuple[list[int], dict[int, tuple[int, int]]]: The layout and the block info
        map (id -> (start_pos, size))
    """
    _id = 0
    res: list[int] = []
    block_info_map: dict[int, tuple[int, int]] = {}  # id -> (start_pos, size)
    pos = 0
    for i, a in enumerate([int(c) for c in s]):
        pos = len(res)
        if i % 2 == 0:
            res.extend([_id] * a)
            block_info_map[_id] = (pos, a)
            _id += 1
        else:
            res.extend([-1] * a)
    return res, block_info_map


def compact_layout2(
    layout: list[int], block_info: dict[int, tuple[int, int]]
) -> list[int]:

    def find_next_empty(start_idx: int) -> int:
        try:
            return layout.index(-1, start_idx)
        except ValueError:
            return -1

    def size_of_empty(start_idx: int) -> int:
        idx = start_idx
        max_idx = len(layout)
        while idx < max_idx and layout[idx] == -1:
            idx += 1
        return idx - start_idx

    def find_acceptable_empty(block_size: int, max_idx: int) -> int:
        idx = find_next_empty(0)
        while idx < max_idx:
            empty_size = size_of_empty(idx)
            if empty_size >= block_size:
                return idx
            idx = find_next_empty(idx + empty_size)
        return -1

    right_id = max(block_info.keys())

    while right_id > 0:
        block_size = block_info[right_id][1]
        # find the largest empty block, starting from the left (idx == 0)
        left = find_acceptable_empty(block_size, block_info[right_id][0])
        if left != -1:
            # move the block from right to the left
            right = block_info[right_id][0]
            data_block = layout[right : right + block_size]  # copy data
            layout[right : right + block_size] = [-1] * block_size  # clear data
            layout[left : left + block_size] = data_block
        right_id -= 1

    return layout


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


def process_layout2(inp: list[str]) -> int:
    layout, data = generate_layout2(inp[0])
    layout = compact_layout2(layout, data)
    total = checksum_layout(layout)
    return total


def part1() -> None:
    apply_lines_from_file("day09.txt", process_layout)


def part2() -> None:
    apply_lines_from_file("day09.txt", process_layout2)


if __name__ == "__main__":
    part2()
