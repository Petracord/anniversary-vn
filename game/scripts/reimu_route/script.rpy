define p = Character("Petra", color="#000000", namebox_style="nameboxPetra")
image petra default = "sprites/petra_gurin.png"

label reimu:

    scene bg room

    show petra default:
        zoom 2.3
        xalign 0.5

    p "You've created a new Ren'Py game."

    p "Once you add a story, pictures, and music, you can release it to the world!"

    return