# Peter
define peter = Character("Peter", image="peter", color="#000000", namebox_style="nameboxPeter")

image peter angry = Image("images/sprites/peter/angry.webp", oversample=2)
image peter default = Image("images/sprites/peter/default.webp", oversample=2)
image peter sad = Image("images/sprites/peter/sad.webp", oversample=2)
image peter smug = Image("images/sprites/peter/smug.webp", oversample=2)
image peter terrified = Image("images/sprites/peter/terrified.webp", oversample=2)
image peter worried = Image("images/sprites/peter/worried.webp", oversample=2)

label expression_test_peter:
    show peter default at center
    pause
    show peter smug
    pause
    show peter worried
    pause
    show peter terrified
    pause
    show peter angry
    pause
    show peter happy # missing
    pause

    jump expression_test