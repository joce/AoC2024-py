from day12 import Land, compute_area_perimeter, compute_price

# ruff: noqa: E741

# cspell:disable
DATA = """AAAA
BBCD
BBCC
EEEC"""

DATA2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""


DATA3 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

DATA4 = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

DATA5 = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
# cspell:enable


def test_compute_area_perimeter():
    lands = compute_area_perimeter([list(row) for row in DATA.split("\n")])
    land_a = next(l for l in lands if l.name == "A")
    assert land_a.area == {(0, 0), (1, 0), (2, 0), (3, 0)}
    assert land_a.perimeter == 10

    land_b = next(l for l in lands if l.name == "B")
    assert land_b.area == {(0, 1), (1, 1), (0, 2), (1, 2)}
    assert land_b.perimeter == 8

    land_c = next(l for l in lands if l.name == "C")
    assert land_c.area == {(2, 1), (2, 2), (3, 2), (3, 3)}
    assert land_c.perimeter == 10

    land_d = next(l for l in lands if l.name == "D")
    assert land_d.area == {(3, 1)}
    assert land_d.perimeter == 4

    land_e = next(l for l in lands if l.name == "E")
    assert land_e.area == {(0, 3), (1, 3), (2, 3)}
    assert land_e.perimeter == 8


def test_compute_area_perimeter2():
    lands = compute_area_perimeter([list(row) for row in DATA2.split("\n")])
    land_o = next(l for l in lands if l.name == "O")
    assert len(land_o.area) == 21
    assert land_o.perimeter == 36
    land_x = [l for l in lands if l.name == "X"]
    assert len(land_x) == 4
    assert all(len(l.area) == 1 for l in land_x)
    assert all(l.perimeter == 4 for l in land_x)


def test_compute_price():
    lands = compute_area_perimeter([list(row) for row in DATA.split("\n")])
    assert sum(compute_price(l) for l in lands) == 140


def test_compute_price2():
    lands = compute_area_perimeter([list(row) for row in DATA2.split("\n")])
    assert sum(compute_price(l) for l in lands) == 772


def test_compute_price3():
    lands = compute_area_perimeter([list(row) for row in DATA3.split("\n")])
    assert sum(compute_price(l) for l in lands) == 1930


def corner_check(lands: list[Land], n: str, expect: int):
    land = next(l for l in lands if l.name == n)
    assert land.corners_cnt == expect


def test_compute_corners():
    lands = compute_area_perimeter([list(row) for row in DATA.split("\n")])
    for l in lands:
        l.find_corners()
    corner_check(lands, "A", 4)
    corner_check(lands, "B", 4)
    corner_check(lands, "C", 8)
    corner_check(lands, "D", 4)
    corner_check(lands, "E", 4)


def test_compute_corners2():
    lands = compute_area_perimeter([list(row) for row in DATA4.split("\n")])
    for l in lands:
        l.find_corners()
    corner_check(lands, "E", 12)
    corner_check(lands, "X", 4)


def test_compute_corners3():
    lands = compute_area_perimeter([list(row) for row in DATA5.split("\n")])
    for l in lands:
        l.find_corners()
    corner_check(lands, "A", 12)
    corner_check(lands, "B", 4)


def test_compute_corners4():
    lands = compute_area_perimeter([list(row) for row in DATA3.split("\n")])
    for l in lands:
        l.find_corners()
    corner_check(lands, "R", 10)
    corner_check(lands, "I", 4)
    corner_check(lands, "C", 22)
    corner_check(lands, "F", 12)
    corner_check(lands, "V", 10)
    corner_check(lands, "J", 12)
    corner_check(lands, "E", 8)
    corner_check(lands, "M", 6)
    corner_check(lands, "S", 6)
