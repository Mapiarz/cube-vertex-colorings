# Cube Vertex Colorings
Simple app for generating and rendering all orbits (i.e. colorings modulo rotations) of cube vertices using
the known 24 octahedron rotational symmetries.

## Installation
POV-Ray must be installed and accessible via `PATH`.

No 3rd party Python dependencies.

Tested on Python 3.11

## Usage
`python app.py number_of_colors`

Between 1 and 4 colors are supported. Can extend that number by adding more colors to `COLOR_MAP` in `rendering.py`.

## Example
All 23 (per Burnside's lemma) distinct 2-color colorings of cube vertices:

<table>
    <tr>
        <td>
            <img  width="128" src="renders/orbit_1.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_2.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_3.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_4.png"/>
        </td>
    </tr>
    <tr>
        <td>
            <img  width="128" src="renders/orbit_5.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_6.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_7.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_8.png"/>
        </td>
    </tr>
    <tr>
        <td>
            <img  width="128" src="renders/orbit_9.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_10.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_11.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_12.png"/>
        </td>
    </tr>
    <tr>
        <td>
            <img  width="128" src="renders/orbit_13.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_14.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_15.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_16.png"/>
        </td>
    </tr>
    <tr>
        <td>
            <img  width="128" src="renders/orbit_17.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_18.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_19.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_20.png"/>
        </td>
    </tr>
    <tr>
        <td>
            <img  width="128" src="renders/orbit_21.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_22.png"/>
        </td>
        <td>
            <img  width="128" src="renders/orbit_23.png"/>
        </td>
    </tr>
</table>


