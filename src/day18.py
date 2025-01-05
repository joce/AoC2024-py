import os
import sys
from queue import PriorityQueue
from typing import NamedTuple


def parse_input(inp: str) -> list[tuple[int, int]]:
    return [
        tuple(map(int, line.split(","))) for line in inp.splitlines()
    ]  # type: ignore


class State(NamedTuple):
    x: int
    y: int


def h(state: State, end_x: int, end_y: int) -> int:
    # Manhattan distance
    return abs(end_x - state.x) + abs(end_y - state.y)


def reconstruct_path(
    came_from: dict[State, State], current: State
) -> list[tuple[int, int]]:
    path: list[tuple[int, int]] = [(current.x, current.y)]
    while current in came_from:
        current = came_from[current]
        path.append((current.x, current.y))
    return path[::-1]


MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
BOUNDS = 71
END = (70, 70)


def solve_astar(
    obstacles: list[tuple[int, int]], end: tuple[int, int], size: int
) -> list[tuple[int, int]] | None:
    start_x, start_y = 0, 0
    end_x, end_y = end
    start_state = State(start_x, start_y)

    open_set: PriorityQueue[tuple[int, State]] = PriorityQueue()
    open_set.put((0, start_state))

    g_score: dict[State, int] = {start_state: 0}
    came_from: dict[State, State] = {}

    while not open_set.empty():
        _, current_state = open_set.get()

        if (current_state.x, current_state.y) == end:
            return reconstruct_path(came_from, current_state)

        for m in MOVES:
            dx, dy = m
            new_x, new_y = current_state.x + dx, current_state.y + dy

            if (new_x, new_y) in obstacles:
                continue

            if (not 0 <= new_x < size) or (not 0 <= new_y < size):
                continue

            new_state = State(new_x, new_y)
            tentative_g = g_score[current_state] + 1

            if tentative_g < g_score.get(new_state, sys.maxsize):
                came_from[new_state] = current_state
                g_score[new_state] = tentative_g
                f_score = tentative_g + h(new_state, end_x, end_y)
                open_set.put((f_score, new_state))

    return None


def part1(d: str) -> None:
    obstacles = parse_input(d)
    path = solve_astar(obstacles[:1024], END, BOUNDS)
    if path is None:
        raise ValueError("No path found")
    print(len(path) - 1)


def part2(d: str) -> None:
    obstacles = parse_input(d)

    low = 1024
    high = len(obstacles)
    path = solve_astar(obstacles[:low], END, BOUNDS)
    if path is None:
        raise ValueError("No path found")
    path = solve_astar(obstacles[:high], END, BOUNDS)
    if path is not None:
        raise ValueError("Path found")

    while (low + 1) < high:
        mid = (low + high) // 2
        path = solve_astar(obstacles[:mid], END, BOUNDS)
        if path:
            low = mid
        else:
            high = mid

    print(obstacles[low])


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "../data/day18.txt")) as f:
        data = f.read()
        part2(data)
