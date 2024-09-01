# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:
    define t = Character("Tutoriella")
    define g = Character("Gameria")
    default rps_wins = 0
    default rps_losses = 0

    scene bg panorama

    jump tutorial