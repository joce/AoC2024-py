from math import floor, log10


def process_input(inputs: list[int]) -> list[int]:
    output: list[int] = []
    for i in inputs:
        if i == 0:
            output.append(1)
        elif floor(log10(i)) % 2 != 0:
            s = str(i)
            mid = len(s) // 2
            output.append(int(s[:mid]))
            output.append(int(s[mid:]))
        else:
            output.append(i * 2024)

    return output


def process_input_2(inputs: list[int], rounds: int) -> int:
    cache: dict[tuple[int, int], int] = {}  # (index, depth) -> result

    def get_res(v: int, depth: int) -> int:
        if (v, depth) in cache:
            return cache[(v, depth)]
        ret = 0
        next_depth = depth - 1
        if depth == 0:
            ret = 1
        else:
            if v == 0:
                ret = get_res(1, next_depth)
            elif floor(log10(v)) % 2 != 0:
                s = str(v)
                mid = len(s) // 2
                ret = get_res(int(s[:mid]), next_depth) + get_res(
                    int(s[mid:]), next_depth
                )
            else:
                ret = get_res(v * 2024, next_depth)

        cache[(v, depth)] = ret
        return ret

    return sum(get_res(i, rounds) for i in inputs)


def part1() -> None:
    inp = [5178527, 8525, 22, 376299, 3, 69312, 0, 275]
    print(process_input_2(inp, 25))


def part2() -> None:
    inp = [5178527, 8525, 22, 376299, 3, 69312, 0, 275]
    print(process_input_2(inp, 75))


if __name__ == "__main__":
    part2()
