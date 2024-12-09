import pytest

from day06 import (
    Direction,
    is_obstacle,
    locate_guard,
    next_dir,
    parse_grid,
    patrol,
    patrol_add_obstacles,
)

SRC: str = """....#.....
              .........#
              ..........
              ..#.......
              .......#..
              ..........
              .#..^.....
              ........#.
              #.........
              ......#..."""


@pytest.fixture(name="data")
def test_data() -> list[list[int]]:
    return parse_grid(SRC)


def test_next_dir():
    assert next_dir(Direction.UP) == Direction.RIGHT
    assert next_dir(Direction.RIGHT) == Direction.DOWN
    assert next_dir(Direction.DOWN) == Direction.LEFT
    assert next_dir(Direction.LEFT) == Direction.UP


def test_locate_guard(data: list[list[int]]):
    assert locate_guard(data) == (4, 6)


def test_is_obstacle(data: list[list[int]]):
    assert is_obstacle(data, 4, 0)
    assert is_obstacle(data, 7, 4)
    assert not is_obstacle(data, 5, 3)
    assert not is_obstacle(data, 4, 6)  # Guard


def test_patrol(data: list[list[int]]):
    assert patrol(data) == 41


def test_patrol_add_obstacles(data: list[list[int]]):
    assert patrol_add_obstacles(data) == 6
