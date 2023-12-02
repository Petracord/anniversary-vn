define rosemi = Character("Rosemi", image="rosemi", color="#000000", namebox_style="nameboxRosemi")

# sprites
image rosemi default = Image("images/sprites/rosemi/default.webp", oversample=2.4)
image rosemi distant = Image("images/sprites/rosemi/distant.webp", oversample=2.4)
image rosemi excited = Image("images/sprites/rosemi/excited.webp", oversample=2.4)
image rosemi happy = Image("images/sprites/rosemi/happy.webp", oversample=2.4)
image rosemi shocked_worried = Image("images/sprites/rosemi/shocked worry.webp", oversample=2.4)
image rosemi shocked = Image("images/sprites/rosemi/shocked.webp", oversample=2.4)
image rosemi worried = Image("images/sprites/rosemi/worried.webp", oversample=2.4)

label expression_test_rosemi:
    show rosemi default at center
    pause
    show rosemi shocked
    pause
    show rosemi worried
    pause
    show rosemi distant
    pause
    show rosemi excited
    pause
    show rosemi happy
    pause
    show rosemi smug # this sprite won't be available for the demo
    pause

    jump expression_test