from day17 import run


def test_computer_1():
    output, _, b, _ = run([2, 6], c=9)
    assert b == 1
    assert not output


def test_computer_2():
    output, _, _, _ = run([5, 0, 5, 1, 5, 4], a=10)
    assert output == [0, 1, 2]


def test_computer_3():
    output, a, _, _ = run([0, 1, 5, 4, 3, 0], a=2024)
    assert output == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]
    assert a == 0


def test_computer_4():
    _, _, b, _ = run([1, 7], b=29)
    assert b == 26


def test_computer_5():
    _, _, b, _ = run([4, 0], b=2024, c=43690)
    assert b == 44354


def test_computer_6():
    output, _, _, _ = run([0, 1, 5, 4, 3, 0], a=729)
    assert output == [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]


def test_computer_7():
    program = [0, 3, 5, 4, 3, 0]
    output, _, _, _ = run(program, a=117440)
    assert output == program
