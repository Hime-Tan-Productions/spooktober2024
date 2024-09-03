# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:
    define t = Character("Tiffany")
    define g = Character("Gabriella")
    define c = Character("Connor")

    $flags = {}

    default beatdown = False

    default winning_streak = 0

    scene bg_street

    jump tutorial