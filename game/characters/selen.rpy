define selen = Character("Selen", color="#000000", namebox_style="nameboxSelen")

image selen happy = Image("images/sprites/selen/Happy.webp", oversample=2.05)
image selen default = Image("images/sprites/selen/Neutral.webp", oversample=2.05)
image selen shocked = Image("images/sprites/selen/Shocked.webp", oversample=2.05)
image selen worried = Image("images/sprites/selen/Worried.webp", oversample=2.05)
image selen excited = Image("images/sprites/selen/Excited.webp", oversample=2.05) # defined excited sprite

label expression_test_selen:
    show selen default at center
    pause
    show selen shocked
    pause
    show selen excited
    pause
    show selen worried
    pause
    show selen sad # won't be available
    pause
    show selen happy
    pause

    jump expression_test