from day19 import can_construct, count_ways, parse_input

DATA = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


def test_parse_input():
    avail, desired = parse_input(DATA)
    assert avail == ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
    assert desired == [
        "brwrr",
        "bggr",
        "gbbr",
        "rrbgbr",
        "ubwu",
        "bwurrg",
        "brgr",
        "bbrgwb",
    ]


def test_can_construct():
    avail, desired = parse_input(DATA)
    count = sum(1 for design in desired if can_construct(design, avail))
    assert count == 6


def test_count_ways():
    avail, desired = parse_input(DATA)
    count = sum(count_ways(design, avail) for design in desired)
    assert count == 16
