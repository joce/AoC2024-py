import os
from typing import TypeAlias, no_type_check

import matplotlib.pyplot as plt
import numpy as np

OBSTACLE = 9
START = 8
END = 7


Maze: TypeAlias = list[list[int]]
Pos: TypeAlias = tuple[int, int]


def parse_track(src: str) -> Maze:
    return [
        [
            (
                START
                if cell == "S"
                else END if cell == "E" else OBSTACLE if cell == "#" else 0
            )
            for cell in line.strip()
        ]
        for line in src.splitlines()
    ]


# pylint: disable=too-many-locals
def create_distance_maps(track: Maze) -> tuple[dict[Pos, int], dict[int, Pos]]:
    # Find start and end positions
    rows, cols = len(track), len(track[0])
    end_pos = (-1, -1)
    start_pos = (-1, -1)
    for i in range(rows):
        for j in range(cols):
            if track[i][j] == END:
                end_pos = (i, j)
            elif track[i][j] == START:
                start_pos = (i, j)

    # Initialize tracking variables
    current = (end_pos, 0)
    prev_pos = None

    # Initialize maps with end position
    pos_to_dist = {end_pos: 0}
    dist_to_pos = {0: end_pos}

    while current[0] != start_pos:
        pos, dist = current

        # Find the single next position
        i, j = pos
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            next_pos = (ni, nj)
            if (
                0 <= ni < rows
                and 0 <= nj < cols
                and track[ni][nj] != OBSTACLE
                and next_pos != prev_pos
            ):
                prev_pos = pos
                current = (next_pos, dist + 1)
                # Add to maps at the end of successful iteration
                pos_to_dist[next_pos] = dist + 1
                dist_to_pos[dist + 1] = next_pos
                break

    return pos_to_dist, dist_to_pos


def count_cheats(
    pos_to_dist: dict[Pos, int], dist_to_pos: dict[int, Pos], min_improvement: int
):
    max_dist = max(dist_to_pos.keys())
    cheat_length = 2  # The distance we travel during cheat
    count = 0

    # Check all positions from start until min_improvement steps before end
    for dist in range(max_dist, min_improvement - 1, -1):
        if dist not in dist_to_pos:
            continue

        current_pos = dist_to_pos[dist]
        i, j = current_pos

        # Check all positions 'cheat_length` steps away in cardinal directions
        for di, dj in [
            (0, cheat_length),
            (cheat_length, 0),
            (0, -cheat_length),
            (-cheat_length, 0),
        ]:
            target_pos = (i + di, j + dj)

            # If target position is in our track
            if target_pos in pos_to_dist:
                target_dist = pos_to_dist[target_pos]

                # Calculate actual improvement
                # Current distance - (target distance + cheat length)
                improvement = dist - (target_dist + cheat_length)

                if improvement >= min_improvement:
                    count += 1

    return count


# pylint: disable=too-many-locals
def count_cheats_2(
    pos_to_dist: dict[Pos, int],
    dist_to_pos: dict[int, Pos],
    min_improvement: int,
    max_cheat_length: int = 20,
):
    max_dist = max(dist_to_pos.keys())
    count = 0

    # pylint: disable=too-many-nested-blocks
    for dist in range(max_dist, min_improvement - 1, -1):
        if dist not in dist_to_pos:
            continue

        current_pos = dist_to_pos[dist]
        i, j = current_pos

        # Check all positions within Manhattan distance max_cheat_length
        for di in range(-max_cheat_length, max_cheat_length + 1):
            for dj in range(
                -max_cheat_length + abs(di), max_cheat_length - abs(di) + 1
            ):
                target_pos = (i + di, j + dj)

                # If target position is in our track
                if target_pos in pos_to_dist:
                    target_dist = pos_to_dist[target_pos]
                    # Manhattan distance = actual steps needed
                    cheat_length = abs(di) + abs(dj)

                    # Verify we're within cheat limit
                    if cheat_length <= max_cheat_length:
                        # Calculate actual improvement
                        improvement = dist - (target_dist + cheat_length)

                        if improvement >= min_improvement:
                            count += 1

    return count


def visualize_track_distances(track: Maze, pos_to_dist: dict[Pos, int]):
    # Create RGB array (initialized to white)
    rows, cols = len(track), len(track[0])
    rgb = np.ones((rows, cols, 3))

    # Find max distance for normalization
    max_dist = max(pos_to_dist.values())

    # Set walls to black
    wall_mask = np.array(track) == OBSTACLE
    rgb[wall_mask] = [0, 0, 0]

    # Set track positions with green gradient
    for pos, dist in pos_to_dist.items():
        i, j = pos
        # Convert distance to saturation (1 at start, 0 at end)
        saturation = dist / max_dist
        # Create green with varying saturation (mixing with white)
        rgb[i, j] = [1 - saturation, 1, 1 - saturation]

    # Set start (yellow) and end (red)
    for i in range(rows):
        for j in range(cols):
            if track[i][j] == START:
                rgb[i, j] = [1, 1, 0]  # Yellow
            elif track[i][j] == END:
                rgb[i, j] = [1, 0, 0]  # Red

    @no_type_check
    def display_plt():
        # Display the image
        plt.figure(figsize=(10, 10))
        plt.imshow(rgb)
        plt.axis("off")
        plt.show()

    display_plt()


def solve():
    with open(os.path.join(os.path.dirname(__file__), "../data/day20.txt")) as f:
        track = parse_track(f.read())
        pos_to_dist, dist_to_pos = create_distance_maps(track)
        cheats_count = count_cheats(pos_to_dist, dist_to_pos, 100)
        print(f"part 1: {cheats_count}")
        cheats_count = count_cheats_2(pos_to_dist, dist_to_pos, 100, 20)
        print(f"part 2: {cheats_count}")


if __name__ == "__main__":
    solve()
