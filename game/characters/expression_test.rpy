# this script helps preview the character sprites and ensure that every sprite is working as intended

label expression_test:
    scene black
    window hide

    menu:
        "Petra":
            jump expression_test_petra
        "Selen":
            jump expression_test_selen
        "Rosemi":
            jump expression_test_rosemi
        "Reimu":
            jump expression_test_reimu
        "Nina":
            jump expression_test_nina
        "Peter":
            jump expression_test_peter
    jump expression_test

