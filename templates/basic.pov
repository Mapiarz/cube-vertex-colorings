#version 3.7;
global_settings { assumed_gamma 1.0 }
#default{ finish{ ambient 0.1 diffuse 0.9 conserve_energy}}

#include "colors.inc"

// Camera, lights, sky
#declare CameraPosition = <12, 10, -16>;
camera{
    location CameraPosition
    look_at  <4, 4, 0>
}

light_source{ <-200, 300, -150> color White * 0.9 shadowless}
light_source{ CameraPosition  color rgb<0.9, 0.9, 1> * 0.1 shadowless}


// Boxes - representing vertices
#declare BoxSize = 4;
#declare BoxSpacing = 4;
#declare BoxPadding = 0.95;

#declare BoxCoordinates = array[2]{
    <0, 0, 0>,
    <BoxSize, BoxSize, BoxSize>
}

#declare CuberVerticeBoxes = union{
    box{
        BoxCoordinates[0] * BoxPadding
        BoxCoordinates[1] * BoxPadding
        $color1
        translate <0, 0, 0> * BoxSpacing
    }

    box{
        BoxCoordinates[0] * BoxPadding
        BoxCoordinates[1] * BoxPadding
        $color2
        translate <1, 0, 0> * BoxSpacing
    }

    box{
        BoxCoordinates[0] * BoxPadding
        BoxCoordinates[1] * BoxPadding
        $color3
        translate <0, 0, 1> * BoxSpacing
    }

    box{
        BoxCoordinates[0] * BoxPadding
        BoxCoordinates[1] * BoxPadding
        $color4
        translate <1, 0, 1> * BoxSpacing
    }

    box{
        BoxCoordinates[0] * BoxPadding
        BoxCoordinates[1] * BoxPadding
        $color5
        translate <0, 1, 0> * BoxSpacing
    }

    box{
        BoxCoordinates[0] * BoxPadding
        BoxCoordinates[1] * BoxPadding
        $color6
        translate <1, 1, 0> * BoxSpacing
    }

    box{
        BoxCoordinates[0] * BoxPadding
        BoxCoordinates[1] * BoxPadding
        $color7
        translate <0, 1, 1> * BoxSpacing
    }

    box{
        BoxCoordinates[0] * BoxPadding
        BoxCoordinates[1] * BoxPadding
        $color8
        translate <1, 1, 1> * BoxSpacing
    }
}

// Draw the vertices
object{
    CuberVerticeBoxes
}
