import pytest

from day06 import (
    is_obstacle,
    is_out_of_bounds,
    locate_guard,
    move_guard,
    patrol,
    patrol_with_new_obstacles,
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
def test_data() -> list[list[str]]:
    return [list(line.strip()) for line in SRC.splitlines()]


def test_locate_guard(data: list[list[str]]):
    assert locate_guard(data) == (4, 6)


def test_is_obstacle(data: list[list[str]]):
    assert is_obstacle(data, 4, 0)
    assert is_obstacle(data, 7, 4)
    assert not is_obstacle(data, 5, 3)
    assert not is_obstacle(data, 4, 6)  # Guard


def test_is_out_of_bounds(data: list[list[str]]):
    assert not is_out_of_bounds(data, 0, 0)
    assert not is_out_of_bounds(data, 6, 4)
    assert is_out_of_bounds(data, -1, 4)
    assert is_out_of_bounds(data, 6, -1)
    assert is_out_of_bounds(data, 10, 4)
    assert is_out_of_bounds(data, 6, 10)


def test_move_guard(data: list[list[str]]):
    x, y = locate_guard(data)
    orig_x = x
    orig_y = y
    guard = (x, y, 0)
    guard = move_guard(data, guard)
    assert data[orig_y][orig_x] == "0"


def test_move_guard_turn_right(data: list[list[str]]):
    x, y = locate_guard(data)
    data[y][x] = "."
    x, y = 4, 1
    data[x][y] = "^"  # place guard in front of obstacle
    orig_x = x
    orig_y = y

    guard = (x, y, 0)
    guard = move_guard(data, guard)
    assert guard[0] == orig_x  # didn't move but turned
    assert guard[1] == orig_y
    assert guard[2] == 1


def test_patrol(data: list[list[str]]):
    assert patrol(data) == 41


def test_has_right_path(data: list[list[str]]):
    assert patrol_with_new_obstacles(data) == 6
