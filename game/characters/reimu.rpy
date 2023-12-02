# Reimu
define reimu = Character("Reimu", color="#000000", namebox_style="nameboxReimu")

image reimu angry = Image("sprites/reimu/angry (hat & bracelet) .webp", oversample=2.15)
image reimu determined = Image("sprites/reimu/determined (hat & bracelet) .webp", oversample=2.15)
image reimu happy = Image("sprites/reimu/laugh (hat & bracelet) .webp", oversample=2.15)
image reimu default = Image("sprites/reimu/neutral (hat & bracelet) .webp", oversample=2.15)
image reimu sad = Image("sprites/reimu/sad (hat & bracelet) .webp", oversample=2.15)
image reimu shy = Image("sprites/reimu/shy (hat & bracelet) .webp", oversample=2.15)
image reimu smile = Image("sprites/reimu/smile (hat & bracelet) .webp", oversample=2.15)

label expression_test_reimu:
    show reimu default at center
    pause
    show reimu surprised # this sprite won't be available for the demo
    pause
    show reimu angry
    pause
    show reimu sad
    pause
    show reimu shy
    pause
    show reimu determined
    pause
    show reimu happy
    pause
    show reimu smile
    pause
    show reimu confused # this sprite won't be available for the demo
    pause

    jump expression_test