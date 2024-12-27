import os
from enum import Enum
from time import perf_counter


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


DIRECTION_LENGTH = len(Direction)

OBSTACLE = 8
GUARD = 9

grid_height = 0  # pylint: disable=invalid-name
grid_width = 0  # pylint: disable=invalid-name


def parse_grid(src: str) -> list[list[int]]:
    return [
        [
            GUARD if char == "^" else OBSTACLE if char == "#" else 0
            for char in line.strip()
        ]
        for line in src.splitlines()
    ]


def next_dir(direction: Direction) -> Direction:
    return Direction((direction.value % DIRECTION_LENGTH) + 1)


def locate_guard(grid: list[list[int]]) -> tuple[int, int]:
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == GUARD:
                return x, y
    return -1, -1


def is_obstacle(grid: list[list[int]], x: int, y: int) -> bool:
    return grid[y][x] == OBSTACLE


def is_out_of_bounds(x: int, y: int) -> bool:
    return x < 0 or y < 0 or y >= grid_height or x >= grid_width


def get_updated_position(x: int, y: int, direction: Direction) -> tuple[int, int]:
    match direction:
        case Direction.UP:
            y -= 1
        case Direction.RIGHT:
            x += 1
        case Direction.DOWN:
            y += 1
        case Direction.LEFT:
            x -= 1
    return x, y


def move_guard(
    grid: list[list[int]], guard: tuple[int, int, Direction]
) -> tuple[int, int, Direction]:
    init_x, init_y, direction = guard
    x, y = get_updated_position(init_x, init_y, direction)

    if is_out_of_bounds(x, y) or not is_obstacle(grid, x, y):
        return x, y, direction

    return init_x, init_y, next_dir(direction)


def patrol(grid: list[list[int]]) -> int:
    global grid_height, grid_width  # pylint: disable=global-statement
    grid_height = len(grid)
    grid_width = len(grid[0])

    x, y = locate_guard(grid)
    direction = Direction.UP
    been_there: set[tuple[int, int, Direction]] = set()
    while not is_out_of_bounds(x, y) and (x, y, direction) not in been_there:
        been_there.add((x, y, direction))
        x, y, direction = move_guard(grid, (x, y, direction))

    if not is_out_of_bounds(x, y):
        return -1

    return len({(x, y) for x, y, _ in been_there})


def patrol_add_obstacles(grid: list[list[int]]) -> int:
    count = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell not in (GUARD, OBSTACLE):
                grid[y][x] = OBSTACLE
                ret = patrol(grid)
                if ret == -1:
                    count += 1
                grid[y][x] = 0

    return count


def part_1() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../data/day06.txt")) as f:
        data = parse_grid(f.read())
        start = perf_counter()
        ret = patrol(data)
        end = perf_counter()
        print(ret)
        print(f"Time: {end - start:.7f}")


def part_2() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../data/day06.txt")) as f:
        data = parse_grid(f.read())
        start = perf_counter()
        ret = patrol_add_obstacles(data)
        end = perf_counter()
        print(ret)
        print(f"Time: {end - start:.7f}")


if __name__ == "__main__":
    part_1()
