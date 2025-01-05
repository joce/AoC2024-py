from day18 import parse_input, solve_astar

DATA = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

BOUNDS = 7
END = (6, 6)


def test_solve_astar():
    obstacles = parse_input(DATA)
    path = solve_astar(obstacles[:12], END, BOUNDS)
    assert path is not None
    assert len(path) - 1 == 22


def test_solve_part_2():
    # we know that at 12, there is a path.
    obstacles = parse_input(DATA)
    path = solve_astar(obstacles[:12], END, BOUNDS)
    assert path is not None

    # Check that at 24, there is no path.
    path = solve_astar(obstacles[: len(obstacles)], END, BOUNDS)
    assert not path

    # Now do a binary search
    low = 12
    high = len(obstacles)
    while (low + 1) < high:
        mid = (low + high) // 2
        path = solve_astar(obstacles[:mid], END, BOUNDS)
        if path:
            low = mid
        else:
            high = mid

    assert obstacles[low] == (6, 1)
