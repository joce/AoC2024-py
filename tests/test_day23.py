from day23 import find_password, find_t_triangles, load_graph

PAIRS = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


def test_find_t_triangles():
    graph = load_graph(PAIRS)
    assert find_t_triangles(graph) == 7


def test_find_password():
    graph = load_graph(PAIRS)
    assert find_password(graph) == "co,de,ka,ta"
