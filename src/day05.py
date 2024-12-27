import os


def parse_input(inp: str) -> tuple[list[tuple[int, int]], list[list[int]]]:

    rows = [r.strip() for r in inp.splitlines()]

    # The dependencies are the lines before we find an empty line
    i = 0
    pairs: list[tuple[int, int]] = []
    for line in rows:
        i += 1
        if len(line) == 0:
            break
        pair: list[int] = [int(v) for v in line.split("|")]
        pairs.append((pair[0], pair[1]))

    # These are now the lists we're required to validate
    data: list[list[int]] = []
    for line in rows[i:]:
        data.append([int(v) for v in line.split(",")])

    return (pairs, data)


def is_valid_sequence(pairs: list[tuple[int, int]], data: list[int]) -> bool:
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if (data[j], data[i]) in pairs:
                return False
    return True


def make_valid_sequence(pairs: list[tuple[int, int]], data: list[int]) -> list[int]:
    while not is_valid_sequence(pairs, data):
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if (data[j], data[i]) in pairs:
                    data[i], data[j] = data[j], data[i]
    return data


def get_mid_value(data: list[int]) -> int:
    return data[len(data) // 2]


def get_sum_of_valid_sequences(
    pairs: list[tuple[int, int]], data: list[list[int]]
) -> int:
    return sum(get_mid_value(d) for d in data if is_valid_sequence(pairs, d))


def get_sum_of_invalid_sequences(
    pairs: list[tuple[int, int]], data: list[list[int]]
) -> int:
    return sum(
        get_mid_value(make_valid_sequence(pairs, d))
        for d in data
        if not is_valid_sequence(pairs, d)
    )


def part_1() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../data/day05.txt")) as f:
        pairs, data = parse_input(f.read())
        ret = get_sum_of_valid_sequences(pairs, data)
        print(ret)


def part_2() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../data/day05.txt")) as f:
        pairs, data = parse_input(f.read())
        ret = get_sum_of_invalid_sequences(pairs, data)
        print(ret)


if __name__ == "__main__":
    part_2()
