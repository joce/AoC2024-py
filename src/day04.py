import os


def find_xmas(data: list[str]) -> int:
    row_cnt = len(data)
    col_cnt = len(data[0])  # assuming a well formed matrix
    directions = [
        (dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx, dy) != (0, 0)
    ]

    word = "XMAS"
    word_len = len(word)

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < row_cnt and 0 <= c < col_cnt

    def check_word(r: int, c: int, dr: int, dc: int) -> bool:
        # First check if the whole word would fit in this direction
        if not all(in_bounds(r + i * dr, c + i * dc) for i in range(word_len)):
            return False
        # Then check if the characters match
        return all(data[r + i * dr][c + i * dc] == char for i, char in enumerate(word))

    return sum(
        check_word(row, col, dr, dc)
        for row in range(row_cnt)
        for col in range(col_cnt)
        for dr, dc in directions
        if data[row][col] == "X"
    )


def find_x_mas(data: list[str]) -> int:
    row_cnt = len(data)
    col_cnt = len(data[0])  # assuming a well formed matrix

    def check_diagonal(r: int, c: int, diag: int) -> bool:
        return {data[r - 1][c - diag], data[r + 1][c + diag]} == {"M", "S"}

    return len(
        [
            (r, c)
            for r in range(1, row_cnt - 1)
            for c in range(1, col_cnt - 1)
            if data[r][c] == "A"
            and check_diagonal(r, c, 1)
            and check_diagonal(r, c, -1)
        ]
    )


def part_1() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day04.txt")) as f:
        ret = find_xmas(f.readlines())
        print(ret)


def part_2() -> None:
    with open(os.path.join(os.path.dirname(__file__), "day04.txt")) as f:
        ret = find_x_mas(f.readlines())
        print(ret)


if __name__ == "__main__":
    part_2()
