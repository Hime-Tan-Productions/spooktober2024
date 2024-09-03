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

    default rps_wins = 0
    default rps_losses = 0

    default coinflip_wins = 0
    default coinflip_losses = 0

    default numberguess_wins = 0
    default numberguess_losses = 0

    scene bg_street

    jump tutorial