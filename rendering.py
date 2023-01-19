from os import remove, system
from string import Template
from typing import NamedTuple

from aliases import VerticePermutation


class Color(NamedTuple):
    red: float
    green: float
    blue: float
    alpha: float


COLOR_MAP: dict[int, Color] = {
    0: Color(0.9, 0.9, 0.9, 0.9),
    1: Color(1, 0, 0, 0.25),
    2: Color(0, 1, 0, 0.25),
    3: Color(0, 0, 1, 0.25),
}


def get_template_context(coloring: VerticePermutation) -> dict[str, str]:
    rgba_coloring = tuple(COLOR_MAP[color] for color in reversed(coloring))
    return {
        f'color{i}': f"pigment{{ color rgbt<{color.red}, {color.green}, {color.blue}, {color.alpha}> }}"
        for i, color 
        in enumerate(rgba_coloring, start=1)
    }

def render_basic(orbit: VerticePermutation, filename_suffix: str) -> None:
    # Read the povray code template
    with open('templates/basic.pov', 'r') as f:
        template_string = f.read()
    
    # Generate the final povray code
    context = get_template_context(orbit)
    povray_template = Template(template_string)
    povray_code = povray_template.substitute(**context)

    # Write the povray code to temporary file
    temp_filename = 'temp.pov'
    with open(temp_filename, 'w') as f: 
        f.write(povray_code)

    # Render the image
    image_size = '2000'
    image_name = f'renders/orbit_{filename_suffix}.png'
    command = f'povray {temp_filename} Height={image_size} Width={image_size} +ua +fn +O{image_name}'
    system(command)

    # Clean up
    remove(temp_filename)