# type: ignore
import os
import sys
from dataclasses import dataclass
from enum import Enum, auto

import networkx as nx

# New solution, using NetworkX (with the help of Claude)


class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    def turn_left(self) -> "Direction":
        return {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH,
        }[self]

    def turn_right(self) -> "Direction":
        return {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
        }[self]

    def get_delta(self) -> tuple[int, int]:
        return {
            Direction.NORTH: (-1, 0),
            Direction.EAST: (0, 1),
            Direction.SOUTH: (1, 0),
            Direction.WEST: (0, -1),
        }[self]


@dataclass(frozen=True)
class Position:
    y: int
    x: int
    facing: Direction


class MazeSolver:
    def __init__(self, maze_str: str):
        self.maze: list[str] = maze_str.strip().split("\n")
        self.height: int = len(self.maze)
        self.width: int = len(self.maze[0])
        self.start: tuple[int, int] = (-1, -1)
        self.end: tuple[int, int] = (-1, -1)
        self.graph: nx.DiGraph | None = None

    def is_walkable(self, y: int, x: int) -> bool:
        return self.maze[y][x] != "#"

    def _create_graph(self) -> nx.DiGraph:
        if self.graph is not None:
            return self.graph

        G = nx.DiGraph()

        for y in range(self.height):
            for x in range(self.width):
                if not self.is_walkable(y, x):
                    continue

                if self.maze[y][x] == "S":
                    self.start = (y, x)
                elif self.maze[y][x] == "E":
                    self.end = (y, x)

                for facing in Direction:
                    current_pos = Position(y, x, facing)

                    # Add edges for turning left and right
                    G.add_edge(
                        current_pos, Position(y, x, facing.turn_left()), weight=1000
                    )
                    G.add_edge(
                        current_pos, Position(y, x, facing.turn_right()), weight=1000
                    )

                    # Add edge for moving forward
                    dy, dx = facing.get_delta()
                    new_y, new_x = y + dy, x + dx

                    if self.is_walkable(new_y, new_x):
                        G.add_edge(
                            current_pos, Position(new_y, new_x, facing), weight=1
                        )

        self.graph = G
        return G

    def _get_minimal_path_info(self) -> tuple[int, list[list[Position]]]:
        G = self._create_graph()
        start_pos = Position(self.start[0], self.start[1], Direction.EAST)
        end_positions = [
            Position(self.end[0], self.end[1], direction) for direction in Direction
        ]

        min_cost: int = sys.maxsize
        all_min_cost_paths: list[list[Position]] = []

        for end_pos in end_positions:
            try:
                path_cost = int(
                    nx.shortest_path_length(G, start_pos, end_pos, weight="weight")
                )

                if path_cost < min_cost:
                    min_cost = path_cost
                    all_min_cost_paths = []

                if path_cost == min_cost:
                    paths = list(
                        nx.all_shortest_paths(G, start_pos, end_pos, weight="weight")
                    )
                    all_min_cost_paths.extend(paths)

            except nx.NetworkXNoPath:
                continue

        if not all_min_cost_paths:
            raise ValueError("No path found from start to end")

        return min_cost, all_min_cost_paths

    def _positions_to_coordinates(self, path: list[Position]) -> list[tuple[int, int]]:
        coordinates = [(pos.x, pos.y) for pos in path]
        unique_coordinates: list[tuple[int, int]] = []
        for coord in coordinates:
            if not unique_coordinates or coord != unique_coordinates[-1]:
                unique_coordinates.append(coord)
        return unique_coordinates

    def get_path_cost(self) -> int:
        min_cost, _ = self._get_minimal_path_info()
        return min_cost

    def get_all_shortest_paths(self) -> list[list[tuple[int, int]]]:
        _, paths = self._get_minimal_path_info()
        return [self._positions_to_coordinates(path) for path in paths]


def part1_2():
    with open(os.path.join(os.path.dirname(__file__), "../data/day16.txt")) as f:
        solver = MazeSolver(f.read())
        cost = solver.get_path_cost()
        print(f"Minimum cost: {cost}")

        all_cells = set()
        for p in solver.get_all_shortest_paths():
            all_cells.update(p)
        print(f"Visited {len(all_cells)} cells")


if __name__ == "__main__":
    part1_2()
