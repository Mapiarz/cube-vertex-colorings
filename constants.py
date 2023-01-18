from typing import List, Tuple


OCTAHEDRON_ROTATIONAL_SYMMETRIES: List[Tuple[int, int, int, int, int, int, int, int]] = [

    # Identity
    (0, 1, 2, 3, 4, 5, 6, 7),
    
    # 3 rotations by 180° around 4-fold axis
    (3, 2, 1, 0, 7, 6, 5, 4),
    (5, 4, 7, 6, 1, 0, 3, 2),
    (6, 7, 4, 5, 2, 3, 0, 1),

    # 8 rotations by 120° around 3-fold axis
    (0, 4, 1, 5, 2, 6, 3, 7),
    (3, 7, 2, 6, 1, 5, 0, 4),
    (5, 1, 4, 0, 7, 3, 6, 2),
    (6, 2, 7, 3, 4, 0, 5, 1),
    (0, 2, 4, 6, 1, 3, 5, 7),
    (3, 1, 7, 5, 2, 0, 6, 4),
    (5, 7, 1, 3, 4, 6, 0, 2),
    (6, 4, 2, 0, 7, 5, 3, 1),

    # 6 rotations by 180° around 2-fold axis
    (4, 6, 5, 7, 0, 2, 1, 3),
    (7, 5, 6, 4, 3, 1, 2, 0),
    (1, 0, 5, 4, 3, 2, 7, 6),
    (7, 6, 3, 2, 5, 4, 1, 0),
    (2, 6, 0, 4, 3, 7, 1, 5),
    (7, 3, 5, 1, 6, 2, 4, 0),

    # 6 rotations by 90° around 4-fold axis
    (1, 3, 0, 2, 5, 7, 4, 6),
    (2, 0, 3, 1, 6, 4, 7, 5),
    (2, 3, 6, 7, 0, 1, 4, 5),
    (4, 5, 0, 1, 6, 7, 2, 3),
    (1, 5, 3, 7, 0, 4, 2, 6),
    (4, 0, 6, 2, 5, 1, 7, 3),
]
"""
List of all 24 octahedron rotational symmetries. Represented by permutations of cube vertices.
Taken from https://en.wikiversity.org/wiki/Full_octahedral_group
"""