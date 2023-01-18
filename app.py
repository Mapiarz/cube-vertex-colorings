import itertools

from aliases import VerticePermutation
from constants import OCTAHEDRON_ROTATIONAL_SYMMETRIES


def rotate_coloring(coloring: VerticePermutation, rotations: list[VerticePermutation]) -> set[VerticePermutation]:
    result: set[VerticePermutation] = set()
    for rotation in rotations:
        result.add(tuple((coloring[i] for i in rotation)))
    return result

def get_orbits(number_of_colors: int) -> set[VerticePermutation]:
    colors: list[int] = list(range(number_of_colors))
    all_colorings: list[VerticePermutation] = list(itertools.product(colors, repeat=8))
    orbits: set[VerticePermutation] = set()
    for coloring in all_colorings:
        rotated_colorings = rotate_coloring(coloring, OCTAHEDRON_ROTATIONAL_SYMMETRIES)
        if not any(rotated_coloring in orbits for rotated_coloring in rotated_colorings):
            orbits.add(coloring)
    return orbits
