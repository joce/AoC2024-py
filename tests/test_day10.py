import pytest

from day10 import trailheads_score

GRID1 = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""

GRID2 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

GRID3 = """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""

GRID4 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

GRID5 = """.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9...."""

GRID6 = """012345
123456
234567
345678
4.6789
56789."""


@pytest.mark.parametrize(
    "inp, expected",
    [(GRID1, 2), (GRID2, 4), (GRID3, 3), (GRID4, 36)],
)
def test_trailheads_score(inp: str, expected: int):
    assert trailheads_score(inp) == expected


@pytest.mark.parametrize(
    "inp, expected",
    [(GRID1, 2), (GRID2, 13), (GRID5, 3), (GRID6, 227), (GRID4, 81)],
)
def test_trailheads_score_count_all(inp: str, expected: int):
    assert trailheads_score(inp, True) == expected
