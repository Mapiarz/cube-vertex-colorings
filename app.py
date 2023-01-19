import sys

from coloring import get_orbits
from rendering import render_basic


args = sys.argv[1:]
assert len(args) == 1
number_of_colors = int(args[0])
assert 4 >= number_of_colors > 0

for i, orbit in enumerate(sorted(get_orbits(number_of_colors)), start=1):
    render_basic(orbit, str(i))
