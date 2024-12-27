import os

#  0 | 1 | 2
# ---+---+---
#  3 | 4 | 5
# ---+---+---
#  6 | 7 | 8

DIRECTIONS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

# cspell:ignore NESW
NESW = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class _Corner:
    def __init__(
        self,
        _1: tuple[int, int],
        _2: tuple[int, int],
        _3: tuple[int, int],
        _4: tuple[int, int],
    ):
        self.definition = (_1, _2, _3, _4)

    def __hash__(self) -> int:
        return hash(self.definition)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, _Corner):
            return NotImplemented
        return self.definition == other.definition


class Land:
    def __init__(self, name: str):
        self.name = name
        self.area: set[tuple[int, int]] = set()
        self.perimeter: int = 0
        self.corners: set[_Corner] = set()
        self.corners_cnt: int = 0

    def find_corners(self) -> int:
        def corner_check(c: _Corner) -> int:
            ins = len([a for a in c.definition if a in self.area])
            if ins in (1, 3):
                return 1
            if ins == 2 and (
                (c.definition[1] in self.area and c.definition[2] in self.area)
                or (c.definition[0] in self.area and c.definition[3] in self.area)
            ):
                return 2
            return 0

        cnt = 0
        corner_indices = [(0, 1, 3, 4), (1, 2, 4, 5), (3, 4, 6, 7), (4, 5, 7, 8)]

        for x, y in self.area:
            around = [(x + d[0], y + d[1]) for d in DIRECTIONS]

            for indices in corner_indices:
                corner = _Corner(*(around[i] for i in indices))
                c = corner_check(corner)
                if c > 0 and corner not in self.corners:
                    cnt += c
                    self.corners.add(corner)

        self.corners_cnt = cnt
        return cnt


def compute_area_perimeter(grid: list[list[str]]) -> list[Land]:
    visited: set[tuple[int, int]] = set()
    lands: list[Land] = []
    height = len(grid)
    width = len(grid[0])

    def in_bounds(x: int, y: int) -> bool:
        return 0 <= x < width and 0 <= y < height

    def explore(v: str, l: Land, x: int, y: int) -> None:  # noqa: E741
        if (x, y) in l.area:
            return
        l.area.add((x, y))
        visited.add((x, y))
        for d in NESW:
            new_x, new_y = x + d[0], y + d[1]
            if not in_bounds(new_x, new_y) or grid[new_y][new_x] != v:
                l.perimeter += 1
            else:
                explore(v, l, new_x, new_y)

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (x, y) not in visited:
                land = Land(cell)
                lands.append(land)
                explore(cell, land, x, y)

    return lands


def compute_price(land: Land) -> int:
    return len(land.area) * land.perimeter


def compute_price2(land: Land) -> int:
    return len(land.area) * land.corners_cnt


def part1():
    with open(os.path.join(os.path.dirname(__file__), "../data/day12.txt")) as f:
        lands = compute_area_perimeter([list(row.strip()) for row in f.readlines()])
        res = sum(compute_price(land) for land in lands)
        print(res)


def part2():
    with open(os.path.join(os.path.dirname(__file__), "../data/day12.txt")) as f:
        lands = compute_area_perimeter([list(row.strip()) for row in f.readlines()])
        for land in lands:
            land.find_corners()
        res = sum(compute_price2(land) for land in lands)
        print(res)


if __name__ == "__main__":
    part2()
