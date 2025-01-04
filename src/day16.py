import os
import sys
from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from queue import PriorityQueue


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


OBSTACLE = 9
START = 8
END = 7


@dataclass(frozen=True)
class State:
    x: int
    y: int
    direction: Direction

    def __lt__(self, other: "State") -> bool:
        return False


def parse_maze(src: str) -> list[list[int]]:
    return [
        [
            (
                START
                if cell == "S"
                else END if cell == "E" else OBSTACLE if cell == "#" else 0
            )
            for cell in line.strip()
        ]
        for line in src.splitlines()
    ]


def find_start(maze: list[list[int]]) -> tuple[int, int]:
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == START:
                return x, y
    raise ValueError("No start found")


def find_end(maze: list[list[int]]) -> tuple[int, int]:
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == END:
                return x, y
    raise ValueError("No start found")


def h(state: State, end_x: int, end_y: int) -> int:
    manhattan_dist = abs(end_x - state.x) + abs(end_y - state.y)

    turns_needed = 0
    if end_x != state.x and end_y != state.y:
        turns_needed = 1

    return manhattan_dist + (turns_needed * 1000)


def reconstruct_path(
    came_from: dict[State, tuple[State, Direction]], current: State
) -> list[Direction]:
    path: list[Direction] = []
    while current in came_from:
        current, direction = came_from[current]
        path.append(direction)
    return path[::-1]


def solve_astar(maze: list[list[int]]) -> list[Direction] | None:
    start_x, start_y = find_start(maze)
    end_x, end_y = find_end(maze)
    start_state = State(start_x, start_y, Direction.EAST)

    NESW: dict[Direction, tuple[int, int]] = {
        Direction.NORTH: (0, -1),
        Direction.EAST: (1, 0),
        Direction.SOUTH: (0, 1),
        Direction.WEST: (-1, 0),
    }

    open_set: PriorityQueue[tuple[int, State]] = PriorityQueue()
    open_set.put((0, start_state))

    came_from: dict[State, tuple[State, Direction]] = {}
    g_score: dict[State, int] = {start_state: 0}

    while not open_set.empty():
        _, current_state = open_set.get()

        if maze[current_state.y][current_state.x] == END:
            return reconstruct_path(came_from, current_state)

        for i in [-1, 0, 1]:
            new_dir = Direction((current_state.direction.value + i) % 4)
            dx, dy = NESW[new_dir]
            new_x, new_y = current_state.x + dx, current_state.y + dy

            if maze[new_y][new_x] == OBSTACLE:
                continue

            new_state = State(new_x, new_y, new_dir)
            turn_cost = 1000 if i != 0 else 0
            tentative_g = g_score[current_state] + 1 + turn_cost

            if tentative_g < g_score.get(new_state, sys.maxsize):
                came_from[new_state] = (current_state, new_dir)
                g_score[new_state] = tentative_g
                f_score = tentative_g + h(new_state, end_x, end_y)
                open_set.put((f_score, new_state))

    return None


def cost_path(path: list[Direction]) -> int:
    return len(path) + 1000 * len([num for num, _ in groupby(path)])


def part1():
    with open(os.path.join(os.path.dirname(__file__), "../data/day16.txt")) as f:
        maze = parse_maze(f.read())
        path = solve_astar(maze)
        if path is not None:
            cost = cost_path(path)
            print(cost)


if __name__ == "__main__":
    part1()
