from day09 import (
    checksum_layout,
    compact_layout,
    compact_layout2,
    generate_layout,
    generate_layout2,
)


def test_generate_layout():
    assert generate_layout("2333133121414131402") == [0, 0, -1, -1, -1, 1, 1, 1, -1, -1, -1, 2, -1, -1, -1, 3, 3, 3, -1, 4, 4, -1, 5, 5, 5, 5, -1, 6, 6, 6, 6, -1, 7, 7, 7, -1, 8, 8, 8, 8, 9, 9]  # fmt: skip


def test_generate_layout2():
    layout, size_map = generate_layout2("2333133121414131402")
    assert layout == [0, 0, -1, -1, -1, 1, 1, 1, -1, -1, -1, 2, -1, -1, -1, 3, 3, 3, -1, 4, 4, -1, 5, 5, 5, 5, -1, 6, 6, 6, 6, -1, 7, 7, 7, -1, 8, 8, 8, 8, 9, 9]  # fmt: skip
    assert size_map == {
        0: (0, 2),
        1: (5, 3),
        2: (11, 1),
        3: (15, 3),
        4: (19, 2),
        5: (22, 4),
        6: (27, 4),
        7: (32, 3),
        8: (36, 4),
        9: (40, 2),
    }


def test_compact_layout():
    layout = generate_layout("2333133121414131402")
    assert compact_layout(layout) == [0, 0, 9, 9, 8, 1, 1, 1, 8, 8, 8, 2, 7, 7, 7, 3, 3, 3, 6, 4, 4, 6, 5, 5, 5, 5, 6, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]  # fmt: skip


def test_compact_layout2():
    layout, data = generate_layout2("2333133121414131402")
    compacted_layout = compact_layout2(layout, data)
    assert compacted_layout == [0, 0, 9, 9, 2, 1, 1, 1, 7, 7, 7, -1, 4, 4, -1, 3, 3, 3, -1, -1, -1, -1, 5, 5, 5, 5, -1, 6, 6, 6, 6, -1, -1, -1, -1, -1, 8, 8, 8, 8, -1, -1]  # fmt: skip


def test_checksum_layout():
    layout = generate_layout("2333133121414131402")
    compact = compact_layout(layout)
    assert checksum_layout(compact) == 1928
