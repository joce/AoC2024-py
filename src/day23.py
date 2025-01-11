# type: ignore
import os

import networkx as nx


def load_graph(pairs: str) -> nx.Graph:
    # Create an empty undirected graph
    graph = nx.Graph()
    graph.add_edges_from(line.split("-") for line in pairs.splitlines())
    return graph


def find_t_triangles(graph: nx.Graph) -> int:
    # Find all triangles and filter for those with 't' nodes
    triangles = [
        clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3
    ]
    t_triangles = [
        clique for clique in triangles if any(node.startswith("t") for node in clique)
    ]

    return len(t_triangles)

    # print(f"Total triangles: {len(triangles)}")
    # print("\nTriangles:")
    # for triangle in sorted(triangles):
    #     print(','.join(sorted(triangle)))

    # print(f"\n\nTriangles with 't' nodes: {len(t_triangles)}")
    # print("\nTriangles with 't' nodes:")
    # for triangle in sorted(t_triangles):
    #     print(','.join(sorted(triangle)))


def find_password(graph: nx.Graph) -> str:
    # Find the largest clique
    max_clique = max(nx.find_cliques(graph), key=len)
    # Sort alphabetically and join with commas as per the password requirements
    return ",".join(sorted(max_clique))


def part1():
    with open(os.path.join(os.path.dirname(__file__), "../data/day23.txt")) as f:
        print(find_t_triangles(load_graph(f.read())))


def part2():
    with open(os.path.join(os.path.dirname(__file__), "../data/day23.txt")) as f:
        print(find_password(load_graph(f.read())))


if __name__ == "__main__":
    part2()
