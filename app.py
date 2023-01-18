from coloring import get_orbits
from rendering import render_basic

for i, orbit in enumerate(sorted(get_orbits(2)), start=1):
    render_basic(orbit, str(i))
