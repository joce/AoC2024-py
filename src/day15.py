import os
from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


ROBOT = 7
OBSTACLE = 8
BOX = 9


def find_first(cells: list[int], target: int) -> int:
    try:
        return cells.index(target)
    except ValueError:
        return -1


def cell_str(cell: int) -> str:
    return (
        "#" if cell == OBSTACLE
        else "O" if cell == BOX
        else "@" if cell == ROBOT
        else "."
    )  # fmt: skip


def move_str(move: Direction) -> str:
    return (
        "^" if move == Direction.UP
        else "v" if move == Direction.DOWN
        else ">" if move == Direction.RIGHT
        else "<"
    )  # fmt: skip


@dataclass
class Robot:
    def __init__(self, x: int, y: int, directions: list[Direction]):
        self.x: int = x
        self.y: int = y
        self.directions: list[Direction] = directions


class Grid:
    MOVES = {
        Direction.UP: (0, -1),
        Direction.RIGHT: (1, 0),
        Direction.DOWN: (0, 1),
        Direction.LEFT: (-1, 0),
    }

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])
        self.start_y = next((i for i, row in enumerate(grid) if ROBOT in row), -1)
        self.start_x = next(
            (i for i, cell in enumerate(grid[self.start_y]) if cell == ROBOT), -1
        )

    def run_robot(self, robot: Robot) -> None:
        # print("\nInitial state:")
        # print(self)
        # print("\n\n=========\n\n")
        for direction in robot.directions:
            # print(f"Move: {move_str(direction)}")
            robot.x, robot.y = self.attempt_move(robot.x, robot.y, direction)
            # print(self)
            # print("\n\n=========\n\n")

    def can_move(self, x: int, y: int, d: Direction) -> bool:
        cells: list[int] = []
        match d:
            case Direction.UP:
                cells = [self.grid[i][x] for i in range(y)]
                cells.reverse()
            case Direction.RIGHT:
                cells = self.grid[y][x + 1 :]
            case Direction.DOWN:
                cells = [self.grid[i][x] for i in range(y + 1, self.h)]
            case Direction.LEFT:
                cells = self.grid[y][:x]
                cells.reverse()
        # I need to return whether there is a 0 before an obstacle
        # get the first 0 and the first obstacle

        space = find_first(cells, 0)
        obstacle = find_first(cells, OBSTACLE)
        return 0 <= space < obstacle

    def attempt_move(self, x: int, y: int, d: Direction) -> tuple[int, int]:
        if self.can_move(x, y, d):
            move = Grid.MOVES[d]
            if self.grid[y + move[1]][x + move[0]]:
                steps = 1
                while self.grid[y + steps * move[1]][x + steps * move[0]] == BOX:
                    steps += 1

                self.grid[y + steps * move[1]][x + steps * move[0]] = BOX

            self.grid[y][x] = 0
            x += move[0]
            y += move[1]
            self.grid[y][x] = ROBOT

        return x, y

    def __str__(self) -> str:
        return "\n".join("".join(cell_str(cell) for cell in row) for row in self.grid)


def parse_input(s: str) -> tuple[Grid, Robot]:
    sl = s.splitlines()
    i = 0
    grid: list[list[int]] = []
    robot_pos = (0, 0)
    while sl[i] != "":
        grid.append([
            OBSTACLE if char == '#'
            else BOX if char == 'O'
            else ROBOT if char == '@'
            else 0
            for char in sl[i]])  # fmt: skip
        if ROBOT in grid[-1]:
            robot_pos = (grid[-1].index(ROBOT), len(grid) - 1)
        i += 1

    directions: list[Direction] = []
    while i < len(sl):
        directions.extend([
            Direction.UP if c == "^"
            else Direction.RIGHT if c == ">"
            else Direction.DOWN if c == "v"
            else Direction.LEFT
            for c in sl[i]])  # fmt: skip
        i += 1

    return Grid(grid), Robot(*robot_pos, directions)


def part1(s: str) -> int:
    grid, robot = parse_input(s)
    grid.run_robot(robot)
    ret = 0
    for i, row in enumerate(grid.grid):
        for j, cell in enumerate(row):
            if cell == BOX:
                ret += i * 100 + j
    return ret


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "../data/day15.txt")) as f:
        print(part1(f.read()))
