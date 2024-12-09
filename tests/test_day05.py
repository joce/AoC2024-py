from day05 import (
    get_sum_of_invalid_sequences,
    get_sum_of_valid_sequences,
    is_valid_sequence,
    make_valid_sequence,
    parse_input,
)

DATA = """7|53
          97|13
          97|61
          97|47
          75|29
          61|13
          75|53
          29|13
          97|29
          53|29
          61|53
          97|53
          61|29
          47|13
          75|47
          97|75
          47|61
          75|61
          47|29
          75|13
          53|1

          75,47,61,53,29
          97,61,53,29,13
          75,29,13
          75,97,47,61,53
          61,13,29
          97,13,75,29,47"""


def test_parse():

    ret = parse_input(DATA)
    assert len(ret[0]) == 21
    assert len(ret[1]) == 6


def test_is_valid():
    data = parse_input(DATA)

    expected = [True, True, True, False, False, False]

    for i, exp in enumerate(expected):
        assert is_valid_sequence(data[0], data[1][i]) == exp


def test_get_sum_of_valid_sequences():
    data = parse_input(DATA)
    assert get_sum_of_valid_sequences(data[0], data[1]) == 143


def test_make_valid_sequence():
    data = parse_input(DATA)

    assert make_valid_sequence(data[0], data[1][3]) == [97, 75, 47, 61, 53]
    assert make_valid_sequence(data[0], data[1][4]) == [61, 29, 13]
    assert make_valid_sequence(data[0], data[1][5]) == [97, 75, 47, 29, 13]


def test_get_sum_of_invalid_sequences():
    data = parse_input(DATA)
    assert get_sum_of_invalid_sequences(data[0], data[1]) == 123
