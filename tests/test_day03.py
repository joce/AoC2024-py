from day03 import (
    find_multiplications,
    find_multiplications_do_dont,
    get_sum,
    get_sum_do_dont,
)


def test_part1():
    inp = r"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    assert find_multiplications(inp) == [
        (2, 4),
        (5, 5),
        (11, 8),
        (8, 5),
    ]

    assert get_sum(inp) == 161


def test_part2():
    inp = r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert find_multiplications_do_dont(inp) == [(2, 4), (8, 5)]
    assert get_sum_do_dont(inp) == 48
