from day13 import parse_inp

DATA = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def test_parse_inp():
    inp = parse_inp(DATA)
    assert len(inp) == 4
    assert inp[0].a == (94, 34)
    assert inp[0].b == (22, 67)
    assert inp[0].p == (8400, 5400)

    assert inp[3].a == (69, 23)
    assert inp[3].b == (27, 71)
    assert inp[3].p == (18641, 10279)


def test_solve_system_integer_large():
    systems = parse_inp(DATA, True)
    assert systems[0].solve_integer() == (None, None)
    assert systems[1].solve_integer() != (None, None)
    assert systems[2].solve_integer() == (None, None)
    assert systems[3].solve_integer() != (None, None)
