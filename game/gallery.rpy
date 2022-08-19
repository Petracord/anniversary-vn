init -10 python:
    def thumbnail(f, w, h):
        return Transform(f, xsize=w, ysize=h, fit="cover")


    def thumbnail_locked(f, w, h):
        return Transform(f, xsize=w, ysize=h, fit="cover", blur = 50, matrixcolor = SaturationMatrix(0))


    def grayed(f):
        return Transform(f, matrixcolor = SaturationMatrix(0))


    def nav_selected(f, name, sel):
        if name == sel:
            return f
        else:
            return grayed(f)


    config.displayable_prefix["thumbnail_l"] = thumbnail_locked


    def cg_button(g, cg, width=300, height=200):
        bttn = g.make_button(cg["name"], thumbnail(cg["source"], width, height), thumbnail_locked(cg["source"], width, height), ysize=height, xsize=width)
        return VBox(bttn, Text("by " + cg["author"], xalign=0, yalign=.5))


    def nav_image(name, ext="", format="png"):
        return "gui/gallery/" + name + ext + "." + format


    full_name = {
        "selen": "Selen Tatsuki",
        "reimu": "Reimu Endou",
        "rosemi": "Rosemi Lovelock"
    }

    character_cgs = {
        "selen": [
            {"source": "placeholder", "name": "selen1", "author": "test1"},
            {"source": "placeholder", "name": "selen2", "author": "test2"},
            {"source": "placeholder", "name": "selen3", "author": "test3"},
            {"source": "placeholder", "name": "selen4", "author": "test4"}
        ],
        "reimu": [
            {"source": "placeholder", "name": "reimu1", "author": ""},
            {"source": "placeholder", "name": "reimu2", "author": ""},
            {"source": "placeholder", "name": "reimu3", "author": ""},
            {"source": "placeholder", "name": "reimu4", "author": ""}
        ],
        "rosemi": [
            {"source": "placeholder", "name": "rosemi1", "author": ""},
            {"source": "placeholder", "name": "rosemi2", "author": ""},
            {"source": "placeholder", "name": "rosemi3", "author": ""},
            {"source": "placeholder", "name": "rosemi4", "author": ""}
        ]
    }

    extras = [
        {
            "title": "Extra: Sprites",
            "cgs": []
        },
        {
            "title": "Extra: Backgrounds",
            "cgs": []
        },
        {
            "title": "Extra: CGs",
            "cgs": []
        }
    ]


init python:
    g = Gallery()

    selected_gallery = None

    # general config
    g.navigation = True
    g.hover_border = '#ffffff40'

    for cgs in character_cgs.values():
        for cg in cgs:
            g.button(cg["name"])

    for cat in extras:
        for cg in cat["cgs"]:
            g.button(cg["name"])

    extra_index = 0


screen gallery:
    tag menu

    # TODO: background
    # add "gallery_background"
    add "#fff"
    
    hbox:
        xfill True

        vbox:
            xoffset 40
            yoffset 120
            
            for i, name in enumerate(["selen", "rosemi", "reimu", "extra", "music"]):
                hbox:
                    yoffset (i * -50)
                    if i % 2 == 1:
                        xoffset 60
                    imagebutton:
                        idle nav_selected(nav_image(name), name, selected_gallery)
                        hover nav_image(name)
                        focus_mask nav_image(name, ext="_mask")
                        action SetVariable("selected_gallery", name)

            hbox:
                yoffset -200
                xalign .5
                textbutton "Return" action Return()

        
        if selected_gallery in ["selen", "rosemi", "reimu"]:
            vbox:
                text full_name[selected_gallery]

                grid 2 2:
                    xfill True

                    for i in range(4):
                        add cg_button(g, character_cgs[selected_gallery][i])
                
        elif selected_gallery == "extra":
            vbox:
                xsize 900
                xalign 1.0
                text extras[extra_index]["title"]

                vpgrid:
                    cols 3
                    spacing 20
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    ysize 900
                    xfill True

                    for i in range(len(extras[extra_index]["cgs"])):
                        add cg_button(g, extras[extra_index]["cgs"])

                grid 3 1:
                    xfill True
                    yalign 1.0

                    if extra_index > 0:
                        textbutton "<< " + extras[extra_index - 1]["title"] xalign 0.0 yalign 0.5 action SetVariable("extra_index", extra_index - 1)
                    else:
                        text ""

                    if extra_index < len(extras) - 1:
                        textbutton extras[extra_index + 1]["title"] + " >>" xalign 1.0 yalign 0.5 action SetVariable("extra_index", extra_index + 1)
                    else:
                        text ""

        elif selected_gallery == "music":
            pass
                
