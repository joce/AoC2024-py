# import pytest

from day01 import compute_similarity_score, find_distance_from_string_list


def test_part1():
    values = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
    res = find_distance_from_string_list(values)
    assert res == 11


def test_part2():
    values = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
    res = compute_similarity_score(values)
    assert res == 31
