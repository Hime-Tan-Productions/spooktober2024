﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("")
define u = Character("???")
define v = Character("Vivienne")
define s = Character("Stephanie")

# The game starts here.
define flags = {}

label start:
    $suspicion = 0
    $max_suspicion = 100
    jump intro
    # init bgm