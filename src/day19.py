import os


def parse_input(s: str) -> tuple[list[str], list[str]]:
    lines = [ln.strip() for ln in s.splitlines()]
    return (lines[0].split(", "), lines[2:])


def can_construct(target: str, patterns: list[str]) -> bool:
    n = len(target)
    # dp[i] represents if we can construct string up to position i
    dp = [False] * (n + 1)
    dp[0] = True  # empty string is always possible

    # For each position in target
    for i in range(n + 1):
        if not dp[i]:
            continue
        # Try each pattern at current position
        for pattern in patterns:
            if target[i:].startswith(pattern):
                dp[i + len(pattern)] = True

    return dp[n]


def count_ways(target: str, patterns: list[str]) -> int:
    n = len(target)
    # dp[i] represents number of ways to construct string up to position i
    dp = [0] * (n + 1)
    dp[0] = 1  # empty string can be made in exactly one way

    for i in range(n + 1):
        if dp[i] == 0:
            continue
        for pattern in patterns:
            if target[i:].startswith(pattern):
                dp[i + len(pattern)] += dp[i]

    return dp[n]


def part1(data: str) -> int:
    avail, desired = parse_input(data)
    return sum(1 for design in desired if can_construct(design, avail))


def part2(data: str) -> int:
    avail, desired = parse_input(data)
    return sum(count_ways(design, avail) for design in desired)


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "../data/day19.txt")) as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
