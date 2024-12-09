import os
from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


OBSTACLE = 8
GUARD = 9


def parse_grid(src: str) -> list[list[int]]:
    return [
        [
            GUARD if char == "^" else OBSTACLE if char == "#" else 0
            for char in line.strip()
        ]
        for line in src.splitlines()
    ]


def next_dir(direction: Direction) -> Direction:
    return Direction((direction.value % len(Direction)) + 1)


def locate_guard(grid: list[list[int]]) -> tuple[int, int]:
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == GUARD:
                return x, y
    return -1, -1


def is_obstacle(grid: list[list[int]], x: int, y: int) -> bool:
    return grid[y][x] == OBSTACLE


def is_out_of_bounds(grid: list[list[int]], x: int, y: int) -> bool:
    return x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0])


def get_updated_position(x: int, y: int, direction: Direction) -> tuple[int, int]:
    if direction == Direction.UP:
        y -= 1
    elif direction == Direction.RIGHT:
        x += 1
    elif direction == Direction.DOWN:
        y += 1
    elif direction == Direction.LEFT:
        x -= 1
    return x, y


def move_guard(
    grid: list[list[int]], guard: tuple[int, int, Direction]
) -> tuple[int, int, Direction]:
    init_x, init_y, direction = guard
    x, y = get_updated_position(init_x, init_y, direction)

    if is_out_of_bounds(grid, x, y):
        grid[init_y][init_x] = direction.value
        return x, y, direction

    if is_obstacle(grid, x, y):
        return init_x, init_y, next_dir(direction)

    grid[init_y][init_x] = direction.value

    return x, y, direction


def patrol(grid: list[list[int]]) -> int:
    x, y = locate_guard(grid)
    direction = Direction.UP
    while not is_out_of_bounds(grid, x, y):
        x, y, direction = move_guard(grid, (x, y, direction))

    direction_values = [d.value for d in Direction]

    return sum(cell in direction_values for row in grid for cell in row)


def part_1() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day06.txt")) as f:
        data = parse_grid(f.read())
        ret = patrol(data)
        print(ret)


if __name__ == "__main__":
    part_1()
