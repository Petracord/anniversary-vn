define nina = Character("Nina", image="nina", color="#000000", namebox_style="nameboxNina")

image nina default = Image("images/sprites/nina/Default.webp", oversample = 1.9)
image nina competitive = Image("images/sprites/nina/competitive.webp", oversample = 1.9)
image nina excited = Image("images/sprites/nina/excited.webp", oversample = 1.9)
image nina happy = Image("images/sprites/nina/happy.webp", oversample = 1.9)
image nina laugh = Image("images/sprites/nina/laugh.webp", oversample = 1.9)
image nina proud = Image("images/sprites/nina/mom.webp", oversample = 1.9)
image nina serious = Image("images/sprites/nina/serious.webp", oversample = 1.9)
image nina smug = Image("images/sprites/nina/smug.webp", oversample = 1.9)
image nina surprised = Image("images/sprites/nina/surprised.webp", oversample = 1.9)
image nina worried = Image("images/sprites/nina/Worried.webp", oversample = 1.9)

label expression_test_nina:
    show nina default at center
    pause
    show nina worried
    pause
    show nina happy
    pause
    show nina excited
    pause
    show nina smug
    pause
    show nina serious
    pause
    show nina proud
    pause
    show nina laugh
    pause
    
    jump expression_test