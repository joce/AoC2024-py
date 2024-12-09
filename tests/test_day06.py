import pytest

from day06 import (
    GUARD,
    Direction,
    is_obstacle,
    is_out_of_bounds,
    locate_guard,
    move_guard,
    next_dir,
    parse_grid,
    patrol,
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


def test_is_out_of_bounds(data: list[list[int]]):
    assert not is_out_of_bounds(data, 0, 0)
    assert not is_out_of_bounds(data, 6, 4)
    assert is_out_of_bounds(data, -1, 4)
    assert is_out_of_bounds(data, 6, -1)
    assert is_out_of_bounds(data, 10, 4)
    assert is_out_of_bounds(data, 6, 10)


def test_move_guard(data: list[list[int]]):
    x, y = locate_guard(data)
    orig_x = x
    orig_y = y
    guard = (x, y, Direction.UP)
    guard = move_guard(data, guard)
    assert data[orig_y][orig_x] == Direction.UP.value


def test_move_guard_turn_right(data: list[list[int]]):
    x, y = locate_guard(data)
    data[y][x] = 0
    x, y = 4, 1
    data[x][y] = GUARD  # place guard in front of obstacle
    orig_x = x
    orig_y = y

    guard = (x, y, Direction.UP)
    guard = move_guard(data, guard)
    assert guard[0] == orig_x  # didn't move but turned
    assert guard[1] == orig_y
    assert guard[2] == Direction.RIGHT


def test_patrol(data: list[list[int]]):
    assert patrol(data) == 41
