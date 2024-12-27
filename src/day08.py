from helper import apply_lines_from_file


def parse_antennas(grid: list[str]) -> dict[str, list[tuple[int, int]]]:
    antennas: dict[str, list[tuple[int, int]]] = {}
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell != ".":
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((x, y))

    return antennas


def is_valid(x: int, y: int, width: int, height: int) -> bool:
    return 0 <= x < width and 0 <= y < height


def find_antinodes(grid: list[str]) -> int:

    antennas_dict = parse_antennas(grid)
    width, height = len(grid[0]), len(grid)

    antinodes: set[tuple[int, int]] = set()

    for _, antennas in antennas_dict.items():
        for i, (x1, y1) in enumerate(antennas):
            for _, (x2, y2) in enumerate(antennas[i + 1 :], start=i + 1):

                x_dist = x2 - x1
                y_dist = y2 - y1

                anti_x: int = x1 - x_dist
                anti_y: int = y1 - y_dist

                if is_valid(anti_x, anti_y, width, height):
                    antinodes.add((anti_x, anti_y))

                anti_x = x2 + x_dist
                anti_y = y2 + y_dist

                if is_valid(anti_x, anti_y, width, height):
                    antinodes.add((anti_x, anti_y))

    return len(antinodes)


def find_antinodes_2(grid: list[str]) -> int:

    antennas_dict = parse_antennas(grid)
    width, height = len(grid[0]), len(grid)

    antinodes: set[tuple[int, int]] = set()

    for _, antennas in antennas_dict.items():
        if len(antennas) < 2:
            continue
        for i, (x1, y1) in enumerate(antennas):
            antinodes.add((x1, y1))
            for _, (x2, y2) in enumerate(antennas[i + 1 :], start=i + 1):

                x_dist = x2 - x1
                y_dist = y2 - y1

                anti_x: int = x1 - x_dist
                anti_y: int = y1 - y_dist

                while is_valid(anti_x, anti_y, width, height):
                    antinodes.add((anti_x, anti_y))
                    anti_x -= x_dist
                    anti_y -= y_dist

                anti_x = x2 + x_dist
                anti_y = y2 + y_dist

                while is_valid(anti_x, anti_y, width, height):
                    antinodes.add((anti_x, anti_y))
                    anti_x += x_dist
                    anti_y += y_dist

    return len(antinodes)


def part_1() -> None:
    apply_lines_from_file("../data/day08.txt", find_antinodes)


def part_2() -> None:
    apply_lines_from_file("../data/day08.txt", find_antinodes_2)


if __name__ == "__main__":
    part_1()
    part_2()
