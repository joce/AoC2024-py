# type: ignore
from day24 import Gate, Wire, get_value, parse, simulate_circuit, zeds

DIAGRAM = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""

DIAGRAM_2 = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""


def test_parse() -> None:
    graph = parse(DIAGRAM)
    assert len(graph.nodes) == 12
    assert len(graph.edges) == 9
    assert len([n for n in graph.nodes if isinstance(n, Wire)]) == 9
    assert len([n for n in graph.nodes if isinstance(n, Gate)]) == 3

    graph = parse(DIAGRAM_2)
    assert len(graph.nodes) == 82
    assert len(graph.edges) == 108
    assert len([n for n in graph.nodes if isinstance(n, Wire)]) == 46
    assert len([n for n in graph.nodes if isinstance(n, Gate)]) == 36


def test_simulate_circuit() -> None:
    graph = parse(DIAGRAM)
    simulate_circuit(graph)
    assert zeds(graph) == [("z00", 0), ("z01", 0), ("z02", 1)]

    graph = parse(DIAGRAM_2)
    simulate_circuit(graph)
    assert zeds(graph) == [
        ("z00", 0),
        ("z01", 0),
        ("z02", 0),
        ("z03", 1),
        ("z04", 0),
        ("z05", 1),
        ("z06", 1),
        ("z07", 1),
        ("z08", 1),
        ("z09", 1),
        ("z10", 1),
        ("z11", 0),
        ("z12", 0),
    ]


def test_get_value() -> None:
    graph = parse(DIAGRAM)
    simulate_circuit(graph)
    assert get_value(zeds(graph)) == 4

    graph = parse(DIAGRAM_2)
    simulate_circuit(graph)
    assert get_value(zeds(graph)) == 2024
