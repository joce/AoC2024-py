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


def part1() -> None:
    inp = [5178527, 8525, 22, 376299, 3, 69312, 0, 275]
    for _ in range(25):
        inp = process_input(inp)

    print(len(inp))


def part2() -> None:
    inp = [5178527, 8525, 22, 376299, 3, 69312, 0, 275]
    for _ in range(75):
        inp = process_input(inp)

    print(len(inp))


if __name__ == "__main__":
    part2()
