import os


def prepare_input(inpt: str) -> list[list[int]]:
    ls = [line.replace(":", "") for line in inpt.splitlines()]
    return [[int(nb) for nb in line.split()] for line in ls]


def try_all(lst: list[int]) -> list[int]:
    if len(lst) == 1:
        return [lst[0]]
    return try_all([lst[0] + lst[1]] + lst[2:]) + try_all([lst[0] * lst[1]] + lst[2:])


def try_all2(lst: list[int]) -> list[int]:
    if len(lst) == 1:
        return [lst[0]]
    return (
        try_all2([lst[0] + lst[1]] + lst[2:])
        + try_all2([lst[0] * lst[1]] + lst[2:])
        + try_all2([int(str(lst[0]) + str(lst[1]))] + lst[2:])  # yuk :-/
    )


def is_valid(data: list[int]) -> bool:
    values = try_all(data[1:])
    return data[0] in values


def is_valid2(data: list[int]) -> bool:
    values = try_all2(data[1:])
    return data[0] in values


def part_1() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day07.txt")) as f:
        data = prepare_input(f.read())
        ret = sum(d[0] for d in data if is_valid(d))
        print(ret)


def part_2() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day07.txt")) as f:
        data = prepare_input(f.read())
        ret = sum(d[0] for d in data if is_valid2(d))
        print(ret)


if __name__ == "__main__":
    part_2()
