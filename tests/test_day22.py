import pytest

from day22 import (
    compute,
    get_all_patterns,
    get_deltas,
    get_last_digits,
    get_max_pattern,
    get_pattern_map,
    mix,
    prune,
)


def test_basics():
    assert mix(42, 15) == 37
    assert prune(100000000) == 16113920


def test_compute():
    secret = 123

    results = [
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254,
    ]

    for result in results:
        secret = compute(secret)
        assert secret == result


@pytest.mark.parametrize(
    "test_input,expected",
    [(1, 8685429), (10, 4700978), (100, 15273692), (2024, 8667524)],
)
def test_2000(test_input: int, expected: int) -> None:
    secret = test_input
    for _ in range(2000):
        secret = compute(secret)
    assert secret == expected


def test_get_last_digits():
    assert get_last_digits(123)[:10] == [3, 0, 6, 5, 4, 4, 6, 4, 4, 2]


def test_get_deltas():
    digits = get_last_digits(123)
    deltas = get_deltas(digits)
    assert deltas[:9] == [-3, 6, -1, -1, 0, 2, -2, 0, -2]
    assert len(deltas) == 2000


def test_get_pattern_map():
    digits = get_last_digits(123)[:10]
    deltas = get_deltas(digits)
    assert get_pattern_map(deltas, digits) == {
        (-3, 6, -1, -1): 4,
        (6, -1, -1, 0): 4,
        (-1, -1, 0, 2): 6,
        (-1, 0, 2, -2): 4,
        (0, 2, -2, 0): 4,
        (2, -2, 0, -2): 2,
    }


def test_get_max_pattern():
    secrets = [1, 2, 3, 2024]
    pat_dict = get_all_patterns(secrets)
    maxv = get_max_pattern(pat_dict)
    assert maxv == 23
