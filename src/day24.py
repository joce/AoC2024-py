# type: ignore
import os
from dataclasses import dataclass
from enum import Enum
from typing import Any

import networkx as nx


class GateType(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"


class NodeType(Enum):
    WIRE = "WIRE"
    GATE = "GATE"


@dataclass
class Node:
    name: str
    type: NodeType

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return self.name == other.name


@dataclass(eq=False)
class Wire(Node):
    value: int | None = None

    def __init__(self, name: str, value: int | None = None):
        super().__init__(name, NodeType.WIRE)
        self.value = value


# pylint: disable=too-few-public-methods
class Gate(Node):
    gate_type: GateType

    def __init__(self, name: str, gate_type: GateType):
        super().__init__(name, NodeType.GATE)
        self.gate_type = gate_type

    def compute(self, input1: int, input2: int) -> int:
        match self.gate_type:
            case GateType.AND:
                return input1 & input2
            case GateType.OR:
                return input1 | input2
            case GateType.XOR:
                return input1 ^ input2


# pylint: disable=too-many-locals
def parse(diag: str) -> nx.DiGraph:
    graph = nx.DiGraph()
    wires: dict[str, Wire] = {}  # cache for wire nodes

    def get_wire(name: str) -> Wire:
        if name not in wires:
            wires[name] = Wire(name)
            graph.add_node(wires[name])
        return wires[name]

    base_wires, gates = [d.splitlines() for d in diag.split("\n\n")]
    for wire in base_wires:
        name, val = wire.split(":")
        w = get_wire(name)
        w.value = int(val)

    for gate in gates:
        a, g, b, _, r = gate.split()
        n1 = get_wire(a)
        n2 = get_wire(b)
        nr = get_wire(r)
        ng = Gate(gate, GateType[g])
        graph.add_node(ng)
        graph.add_edge(n1, ng)
        graph.add_edge(n2, ng)
        graph.add_edge(ng, nr)

    return graph


def simulate_circuit(graph: nx.DiGraph) -> None:
    # Process nodes in topological order
    for node in nx.topological_sort(graph):
        # Skip if it's not a gate
        if not isinstance(node, Gate):
            continue

        # Get input wires (predecessors in the graph)
        input_wires = list(graph.predecessors(node))
        # Get output wire (successor in the graph)
        output_wire = list(graph.successors(node))[0]

        # Compute result and set output wire value
        result = node.compute(input_wires[0].value, input_wires[1].value)
        output_wire.value = result


def zeds(graph: nx.DiGraph) -> list[tuple[str, int]]:
    ret = [
        (n.name, n.value)
        for n in graph.nodes
        if isinstance(n, Wire) and n.name.startswith("z")
    ]
    ret.sort()
    return ret


def get_value(zee: list[tuple[str, int]]) -> int:
    v = 0
    for i, z in enumerate(zee):
        v |= z[1] << i
    return v


def part1(diag: str) -> int:
    graph = parse(diag)
    simulate_circuit(graph)
    return get_value(zeds(graph))


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "../data/day24.txt")) as f:
        print(part1(f.read()))
