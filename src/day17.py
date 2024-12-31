from enum import Enum


class Instruct(Enum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


def run(
    program: list[int], a: int = 0, b: int = 0, c: int = 0
) -> tuple[list[int] | None, int, int, int]:
    reg_a = a
    reg_b = b
    reg_c = c
    counter = 0
    output: list[int] = []
    prog_len = len(program)

    def combo(value: int) -> int:
        if 0 <= value <= 3:
            return value
        if value == 4:
            return reg_a
        if value == 5:
            return reg_b
        if value == 6:
            return reg_c

        raise ValueError("Unsupported combo value")

    while counter + 1 < prog_len:
        opcode = Instruct(program[counter])
        operand = program[counter + 1]
        match opcode:
            case Instruct.ADV:
                reg_a //= 2 ** combo(operand)
            case Instruct.BXL:
                reg_b ^= operand
            case Instruct.BST:
                reg_b = combo(operand) % 8
            case Instruct.JNZ:
                counter = counter + 2 if reg_a == 0 else operand
            case Instruct.BXC:
                reg_b ^= reg_c
            case Instruct.OUT:
                output.append(combo(operand) % 8)
            case Instruct.BDV:
                reg_b = reg_a // (2 ** combo(operand))
            case Instruct.CDV:
                reg_c = reg_a // (2 ** combo(operand))

        if opcode != Instruct.JNZ:
            counter += 2

    return output, reg_a, reg_b, reg_c


def part1():
    output, _, _, _ = run([2, 4, 1, 7, 7, 5, 1, 7, 0, 3, 4, 1, 5, 5, 3, 0], a=66752888)
    print(output)


def part2():
    pass


if __name__ == "__main__":
    part1()
