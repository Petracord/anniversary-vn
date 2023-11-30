define petra = Character("Petra", image="petra", color="#000000", namebox_style="nameboxPetra")

image petra angry = Image("images/sprites/petra/angry.webp", oversample=2)
image petra annoyed = Image("images/sprites/petra/annoyed.webp", oversample=2)
image petra anxious = Image("images/sprites/petra/anxioussad.webp", oversample=2)
image petra deadpan = Image("images/sprites/petra/deadpan.webp", oversample=2)
image petra default = Image("images/sprites/petra/def.webp", oversample=2)
image petra sad = Image("images/sprites/petra/sad.webp", oversample=2)
image petra shocked = Image("images/sprites/petra/shocked.webp", oversample=2)
image petra shy = Image("images/sprites/petra/shy.webp", oversample=2)
image petra softsadsmile = Image("images/sprites/petra/softsadsmile.webp", oversample=2)
image petra thinking = Image("images/sprites/petra/thinking.webp", oversample=2)

label expression_test_petra:
    show petra default at center
    pause
    show petra shy
    pause
    show petra anxious
    pause
    show petra shocked
    pause
    show petra thinking
    pause
    show petra angry
    pause
    show petra sad
    pause
    show petra softsadsmile
    pause
    show petra annoyed
    pause
    show petra deadpan
    pause
    show petra confused # missing
    pause
    show petra terrified # missing
    pause
    show petra scared # missing
    pause

    jump expression_test