# Spaces `count` characters evenly on screen, placing the current character in position `slot` (1-count)
transform spread(count, slot, zoom_level=1.5):
    zoom zoom_level
    anchor (0.5, 0.65)
    ypos 1.0
    xpos (slot / (count + 1))


transform rosemi_bump:
    yoffset -150    

transform bump_right(dist):
    xoffset dist

# miscelaneous positions 
transform outer_left:
    zoom 1.5
    anchor (0.0, 0.65)
    ypos 1.0
    xpos 0.1

transform left:
    zoom 1.5
    anchor (0.5, 0.65)
    ypos 1.0
    xpos 0.25

transform slightleft:
    zoom 1.5
    anchor (0.5, 0.65)
    ypos 1.0
    xpos 0.33

transform center:
    zoom 1.5
    anchor (0.5, 0.65)
    ypos 1.0
    xpos 0.5

transform slightright:
    zoom 1.5
    anchor (0.5, 0.65)
    ypos 1.0
    xpos 0.66

transform right:
    zoom 1.5
    anchor (0.5, 0.65)
    ypos 1.0
    xpos 0.75
    
transform outer_right:
    zoom 1.5
    anchor (1.0, 0.65)
    ypos 1.0
    xpos 1.0
