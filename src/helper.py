import os
from typing import Callable


def apply_lines_from_file(filename: str, func: Callable[[list[str]], int]) -> None:
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        print(func([line.strip() for line in f.readlines()]))


def apply_grid_from_file(filename: str, func: Callable[[list[list[str]]], int]) -> None:
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        print(func([list(line.strip()) for line in f.readlines()]))
