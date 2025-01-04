from day16 import END, START, cost_path, parse_maze, solve_astar

MAZE = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

MAZE_2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""


def test_parse_maze():
    maze = parse_maze(MAZE)
    assert maze[1][13] == END
    assert maze[13][1] == START


def test_solve():
    maze = parse_maze(MAZE)
    res = solve_astar(maze)

    assert res is not None
    assert cost_path(res) == 7036


def test_solve_2():
    maze = parse_maze(MAZE_2)
    res = solve_astar(maze)
    assert res is not None
    assert cost_path(res) == 11048
