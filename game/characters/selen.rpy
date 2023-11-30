define selen = Character("Selen", color="#000000", namebox_style="nameboxSelen")

image selen happy = Image("images/sprites/selen/Happy.webp", oversample=2)
image selen default = Image("images/sprites/selen/Neutral.webp", oversample=2)
image selen shocked = Image("images/sprites/selen/Shocked.webp", oversample=2)
image selen worried = Image("images/sprites/selen/Worried.webp", oversample=2)

label expression_test_selen:
    show selen default at center
    pause
    show selen shocked
    pause
    show selen excited # missing
    pause
    show selen worried
    pause
    show selen sad # missing
    pause
    show selen happy
    pause

    jump expression_test