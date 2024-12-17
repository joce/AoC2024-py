import os


def can_move(x: int, y: int, dir_x: int, dir_y: int, grid: list[list[int]]) -> bool:
    new_x, new_y = x + dir_x, y + dir_y
    return (
        0 <= new_x < len(grid[0])
        and 0 <= new_y < len(grid)
        and grid[new_y][new_x] == grid[y][x] + 1
    )


def trailhead_score(
    x: int, y: int, grid: list[list[int]], visited: set[tuple[int, int]] | None
) -> int:
    if grid[y][x] == 9 or (visited and (x, y) not in visited):
        if visited:
            visited.add((x, y))
        return 1
    score = 0
    for dir_x, dir_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # clockwise
        if can_move(x, y, dir_x, dir_y, grid):
            score += trailhead_score(x + dir_x, y + dir_y, grid, visited)
    return score


def trailheads_score(grid: str, count_all: bool = False) -> int:
    res = 0
    g = [[int(c) if c.isdigit() else -1 for c in line] for line in grid.splitlines()]
    for y in range(len(g)):
        for x in range(len(g[0])):
            if g[y][x] == 0:
                res += trailhead_score(x, y, g, set() if not count_all else None)

    return res


def part_1() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day10.txt")) as f:
        print(trailheads_score(f.read()))


def part_2() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day10.txt")) as f:
        print(trailheads_score(f.read(), True))


if __name__ == "__main__":
    part_2()
