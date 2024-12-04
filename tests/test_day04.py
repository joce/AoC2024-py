from day04 import find_x_mas, find_xmas


def test_part1():
    data = """MMMSXXMASM
              MSAMXMSMSA
              AMXSXMAAMM
              MSAMASMSMX
              XMASAMXAMM
              XXAMMXXAMA
              SMSMSASXSS
              SAXAMASAAA
              MAMMMXMMMM
              MXMXAXMASX"""
    rows = [r.strip() for r in data.splitlines()]

    assert find_xmas(rows) == 18


def test_part2():
    data = """MMMSXXMASM
              MSAMXMSMSA
              AMXSXMAAMM
              MSAMASMSMX
              XMASAMXAMM
              XXAMMXXAMA
              SMSMSASXSS
              SAXAMASAAA
              MAMMMXMMMM
              MXMXAXMASX"""
    rows = [r.strip() for r in data.splitlines()]

    assert find_x_mas(rows) == 9
