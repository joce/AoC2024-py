from day20 import count_cheats, count_cheats_2, create_distance_maps, parse_track

TRACK = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


def test_count_cheats():
    track = parse_track(TRACK)
    pos_to_dist, dist_to_pos = create_distance_maps(track)
    evaluated_cheats = count_cheats(pos_to_dist, dist_to_pos, 2)
    assert evaluated_cheats == 44


def test_count_cheats_2():
    track = parse_track(TRACK)
    pos_to_dist, dist_to_pos = create_distance_maps(track)
    evaluated_cheats = count_cheats_2(pos_to_dist, dist_to_pos, 50, 20)
    assert evaluated_cheats == 285
