"""the cave module can be used to generate random caves map (e.g: video game level layouts)."""

import random


def generate_cave(size_x: int = 256, size_y: int = 256, density: float = 0.45, iterations: int = 5) -> list[list]:
    """generate a cave of the given size.

    :param size_x: The size of the generated cave (X coordinate).
    :param size_y: The size of the generated cave (Y coordinate).
    :param density: The density of the initialization cave (% of walls), should be contained in [0.0, 1.0].
    :param iterations: The number of iterations of cellular automata algorithm to do in order to generate the cave.
    :return: A matrix of 0s and 1s representing the cave (0 represents a path, 1 represents a wall)
    """

    cave = _init_cave(size_x, size_y, density)
    for i in range(iterations):
        cave = _iterate_ca(cave, size_y, size_x)

    return cave


def _init_cave(size_x, size_y, density):
    return [[0 if random.random() >= density else 1 for _ in range(size_y)] for _ in range(size_x)]


def _iterate_ca(cave, size_y, size_x):
    new_map = []
    for i in range(size_y):
        new_line = []

        for j in range(size_x):
            neighbors_count = _neighborhood_walls_count(cave, i, j, size_y, size_x)
            if neighbors_count < 4:
                new_line.append(0)
            elif neighbors_count > 4:
                new_line.append(1)
            else:
                new_line.append(cave[i][j])
        new_map.append(new_line)

    return new_map


def _neighborhood_walls_count(cave, i, j, size_y, size_x):
    neighboring_walls_count = 0

    for di in range(-1, 2):
        for dj in range(-1, 2):
            if not (di == dj == 0):
                if 0 <= i + di < size_y and 0 <= j + dj < size_x:
                    if cave[i + di][j + dj] == 1:
                        neighboring_walls_count += 1
                else:
                    neighboring_walls_count += 1

    return neighboring_walls_count
