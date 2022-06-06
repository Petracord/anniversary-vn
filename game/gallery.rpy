init -10 python:
    def thumbnail(f):
        return Transform(f, xsize=600, ysize=300, fit="contain")


    def thumbnail_locked(f):
        return Transform(f, xsize=600, ysize=300, fit="contain", blur = 50, matrixcolor = SaturationMatrix(0))

    config.displayable_prefix["thumbnail_l"] = thumbnail_locked

    def cg_button(g, cg):
        cg_file = cg["source"]

        bttn = g.make_button(cg["name"], thumbnail(cg_file), thumbnail_locked(cg_file), xalign=.5, yalign=.5)

        return VBox(bttn, Text("Test", xalign=.5, yalign=.5))

init python:
    g = Gallery()

    cgs = [{"name": "petra_design", "source": "petra_designsheet.webp", "locked": True}] * 9

    # general config
    g.navigation = True
    g.hover_border = '#ffffff40'

    for cg in cgs:
        g.button(cg["name"])
        if cg["locked"]:
            g.unlock(cg["name"])

screen gallery:
    tag menu

    # TODO: background
    # add "gallery_background"


    vbox:
        grid 3 3:
            xfill True
            ysize 1000
            for i in range(9):
                add cg_button(g, cgs[i])

        textbutton "Return" action Return() xalign 0.5 yalign 0.5
