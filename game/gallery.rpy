init -10 python:
    def thumbnail(f):
        return Transform(f, zoom = .1852)

    config.displayable_prefix["thumbnail"] = thumbnail

    def thumbnail_locked(f):
        return Transform(f, blur = 50, zoom=.1852, matrixcolor = SaturationMatrix(0))

    config.displayable_prefix["thumbnail_l"] = thumbnail_locked

init python:
    g = Gallery()

    # general config
    g.navigation = True
    g.hover_border = '#ffffff40'

    g.button("petra_design")
    g.image("petra_designsheet")

    g.button("petra_design_locked")
    g.image("petra_designsheet")
    g.unlock("petra_design_locked")

screen gallery:
    tag menu

    # TODO: background
    # add "gallery_background"


    grid 3 3:
        xfill True
        yfill True

        add g.make_button("petra_design", "thumbnail:petra_designsheet.webp", "thumbnail_l:petra_designsheet.webp", xalign=.5, yalign=.5)
        add g.make_button("petra_design_locked", "thumbnail:petra_designsheet.webp", "thumbnail_l:petra_designsheet.webp", xalign=.5, yalign=.5)
        add g.make_button("petra_design_locked", "thumbnail:petra_designsheet.webp", "thumbnail_l:petra_designsheet.webp", xalign=.5, yalign=.5)
        add g.make_button("petra_design_locked", "thumbnail:petra_designsheet.webp", "thumbnail_l:petra_designsheet.webp", xalign=.5, yalign=.5)
        add g.make_button("petra_design_locked", "thumbnail:petra_designsheet.webp", "thumbnail_l:petra_designsheet.webp", xalign=.5, yalign=.5)
        add g.make_button("petra_design_locked", "thumbnail:petra_designsheet.webp", "thumbnail_l:petra_designsheet.webp", xalign=.5, yalign=.5)
        add g.make_button("petra_design_locked", "thumbnail:petra_designsheet.webp", "thumbnail_l:petra_designsheet.webp", xalign=.5, yalign=.5)
        add g.make_button("petra_design_locked", "thumbnail:petra_designsheet.webp", "thumbnail_l:petra_designsheet.webp", xalign=.5, yalign=.5)
        add g.make_button("petra_design_locked", "thumbnail:petra_designsheet.webp", "thumbnail_l:petra_designsheet.webp", xalign=.5, yalign=.5)

#        textbutton "Return" action Return() xalign 0.5 yalign 0.5
