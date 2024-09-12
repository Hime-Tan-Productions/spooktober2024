# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("", color="#ffd73a")
define p = Character("", color="#ffd73a")
define u = Character("???", color="#ffd73a")
define v = Character("Vivienne", color="#ffd73a")
define s = Character("Stephanie", color="#ffd73a")

label start:
    $ flags = {}
    $suspicion = 0
    $max_suspicion = 100
    show screen suspicion_bar
    jump intro
