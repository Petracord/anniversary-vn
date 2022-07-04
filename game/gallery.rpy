init -10 python:
    def thumbnail(f):
        return Transform(f, xsize=600, ysize=400, fit="contain")


    def thumbnail_locked(f):
        return Transform(f, xsize=600, ysize=400, fit="contain", blur = 50, matrixcolor = SaturationMatrix(0))


    def grayed(f):
        return Transform(f, matrixcolor = SaturationMatrix(0))


    def nav_selected(f, name, sel):
        if name == sel:
            return f
        else:
            return grayed(f)


    config.displayable_prefix["thumbnail_l"] = thumbnail_locked


    def cg_button(g, cgs, i):
        cg_file = cgs[i]["source"] if i in cgs else "placeholder"
        bttn = g.make_button(cg["name"], thumbnail(cg_file), thumbnail_locked(cg_file), xalign=.5, yalign=.5)
        return VBox(bttn, Text("Test", xalign=.5, yalign=.5))


    def nav_image(name, ext="", format="png"):
        return "gui/gallery/" + name + ext + "." + format


    full_name = {
        "selen": "Selen Tatsuki",
        "reimu": "Reimu Endou",
        "rosemi": "Rosemi Lovelock"
    }

    character_cgs = {
        "selen": [],
        "reimu": [],
        "rosemi": []
    }


init python:
    g = Gallery()

    cgs = [{"name": "petra_design", "source": "petra_designsheet.webp", "locked": True}] * 9

    selected_gallery = None

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
    add "#fff"
    
    hbox:
        vbox:
            for name in ["selen", "rosemi", "reimu", "extra", "music"]:
                imagebutton:
                    idle nav_selected(nav_image(name), name, selected_gallery)
                    hover nav_image(name)
                    focus_mask nav_image(name, ext="_mask")
                    action SetVariable("selected_gallery", name)
        
        if selected_gallery in ["selen", "rosemi", "reimu"]:
            vbox:
                text full_name[selected_gallery]

                grid 2 2:
                    xfill True

                    for i in range(4):
                        add cg_button(g, character_cgs[selected_gallery], i)

                textbutton "Return" action Return() xalign 0.5 yalign 0.5
                
        elif selected_gallery == "extra":
            vbox:
                text "Extra" # TODO

                vpgrid:
                    cols 3
                    spacing 20
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    ysize 900
                    xfill True

                    for i in range(20):
                        add cg_button(g, [], i)

                textbutton "Return" action Return() xalign 0.5 yalign 0.5

        elif selected_gallery == "music":
            pass
        else:
            vbox:
                grid 3 3:
                    xfill True
                    ysize 1000
                    for i in range(9):
                        add cg_button(g, cgs, i)

                textbutton "Return" action Return() xalign 0.5 yalign 0.5
