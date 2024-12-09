import pytest

from day07 import is_valid, is_valid2, prepare_input, try_all

SRC: str = """190: 10 19
              3267: 81 40 27
              83: 17 5
              156: 15 6
              7290: 6 8 6 15
              161011: 16 10 13
              192: 17 8 14
              21037: 9 7 18 13
              292: 11 6 16 20"""


@pytest.fixture(name="data")
def test_data() -> list[list[int]]:
    return prepare_input(SRC)


def test_prepare_input():
    assert prepare_input(SRC)[4] == [7290, 6, 8, 6, 15]
    assert prepare_input(SRC)[8] == [292, 11, 6, 16, 20]


def test_try_all(data: list[list[int]]):
    assert try_all(data[0][1:]) == [29, 190]
    assert try_all(data[1][1:]) == [148, 3267, 3267, 87480]


def test_is_valid(data: list[list[int]]):
    valid = [0, 1, 8]
    for i, d in enumerate(data):
        assert is_valid(d) == (i in valid)


def test_is_valid2(data: list[list[int]]):
    valid = [0, 1, 3, 4, 6, 8]
    for i, d in enumerate(data):
        assert is_valid2(d) == (i in valid)
