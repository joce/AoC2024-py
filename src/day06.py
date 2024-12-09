import os


def locate_guard(grid: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "^":
                return x, y
    raise ValueError("Guard not found")


def is_obstacle(grid: list[list[str]], x: int, y: int) -> bool:
    return grid[y][x] == "#"


def is_out_of_bounds(grid: list[list[str]], x: int, y: int) -> bool:
    return y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0])


def move_guard(
    grid: list[list[str]], guard: tuple[int, int, int]
) -> tuple[int, int, int]:  # x, y, direction
    init_x = x = guard[0]
    init_y = y = guard[1]
    direction = guard[2]
    if direction == 0:  # up
        y -= 1
    elif direction == 1:  # right
        x += 1
    elif direction == 2:  # down
        y += 1
    elif direction == 3:  # left
        x -= 1

    if is_out_of_bounds(grid, x, y):
        grid[init_y][init_x] = "0"
        return x, y, direction

    if is_obstacle(grid, x, y):
        return init_x, init_y, (direction + 1) % 4

    grid[init_y][init_x] = "0"
    grid[y][x] = "^"
    return x, y, direction


def patrol(grid: list[list[str]]) -> int:
    x, y = locate_guard(grid)
    direction = 0
    while not is_out_of_bounds(grid, x, y):
        x, y, direction = move_guard(grid, (x, y, direction))

    return sum(line.count("0") for line in grid)


def part_1() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day06.txt")) as f:
        print(patrol([list(line.strip()) for line in f.readlines()]))


if __name__ == "__main__":
    part_1()
