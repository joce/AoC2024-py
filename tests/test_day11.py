from day11 import process_input, process_input_2


def test_process():
    assert process_input([0, 1, 10, 99, 999]) == [1, 2024, 1, 0, 9, 9, 2021976]

    inp = [125, 17]
    for _ in range(25):
        inp = process_input(inp)
    assert len(inp) == 55312

    inp = [0]
    for _ in range(75):
        inp = process_input(inp)
    print(len(inp))


def test_process_2():
    assert process_input_2([125, 17], 25) == 55312
