from copy import deepcopy

from helper import apply_grid_from_file


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


def get_updated_position(x: int, y: int, direction: int) -> tuple[int, int]:
    if direction == 0:  # up
        y -= 1
    elif direction == 1:  # right
        x += 1
    elif direction == 2:  # down
        y += 1
    elif direction == 3:  # left
        x -= 1
    return x, y


def move_guard(
    grid: list[list[str]], guard: tuple[int, int, int]
) -> tuple[int, int, int]:  # x, y, direction
    init_x = x = guard[0]
    init_y = y = guard[1]
    direction = guard[2]
    x, y = get_updated_position(x, y, direction)

    if is_out_of_bounds(grid, x, y):
        grid[init_y][init_x] = str(direction)
        return x, y, direction

    if is_obstacle(grid, x, y):
        return init_x, init_y, (direction + 1) % 4

    grid[init_y][init_x] = str(direction)
    # grid[y][x] = "^"
    return x, y, direction


def patrol(grid: list[list[str]]) -> int:
    x, y = locate_guard(grid)
    direction = 0
    while not is_out_of_bounds(grid, x, y):
        x, y, direction = move_guard(grid, (x, y, direction))

    return sum(line.count(str(i)) for line in grid for i in range(4))


def is_patrol_loop(
    grid: list[list[str]], start_x: int, start_y: int, start_dir: int
) -> bool:
    x, y = start_x, start_y
    direction = start_dir
    while not is_out_of_bounds(grid, x, y):
        x, y, direction = move_guard(grid, (x, y, direction))
        if (x, y, direction) == (start_x, start_y, start_dir):
            return True
    return False


def patrol_with_new_obstacles(grid: list[list[str]]) -> int:
    x, y = locate_guard(grid)
    start_x, start_y = x, y
    direction = 0
    new_obstacles: list[tuple[int, int]] = []
    while True:
        obstacle_x, obstacle_y = get_updated_position(x, y, direction)
        if (
            not is_out_of_bounds(grid, obstacle_x, obstacle_y)
            and not is_obstacle(grid, obstacle_x, obstacle_y)
            and (obstacle_x, obstacle_y) != (start_x, start_y)
        ):
            attempt = deepcopy(grid)
            attempt[obstacle_y][obstacle_x] = "#"
            if is_patrol_loop(attempt, x, y, direction):
                new_obstacles.append((obstacle_x, obstacle_y))

        x, y, direction = move_guard(grid, (x, y, direction))
        if is_out_of_bounds(grid, x, y):
            break

    return len(new_obstacles)


def part_1() -> None:
    apply_grid_from_file("day06.txt", patrol)


def part_2() -> None:
    apply_grid_from_file("day06.txt", patrol_with_new_obstacles)


if __name__ == "__main__":
    part_1()
    part_2()
