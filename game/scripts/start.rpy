﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("", color="#ffd73a")
define u = Character("???", color="#ffd73a")
define v = Character("Vivienne", color="#ffd73a")
define s = Character("Stephanie", color="#ffd73a")

# The game starts here.
define flags = {}

label start:
    $suspicion = 0
    $max_suspicion = 100
    jump intro
    # init bgm