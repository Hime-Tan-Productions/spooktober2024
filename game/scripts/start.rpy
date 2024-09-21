# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character(name=None, color="#ffd73a")
define p = Character(name=None, color="#ffd73a")
define u = Character("???", color="#ffd73a")
define v = Character("Vivienne", color="#ffd73a")
define s = Character("Stephanie", color="#ffd73a")

label start:
    $flags = {}
    $journal_people = []
    $journal_story = []
    $journal_todo = []
    $part = 0
    $suspicion = 0
    $max_suspicion = 100
    scene black with fade
    #show screen journal_tabs with moveinleft
    show screen suspicion_bar with moveintop
    jump intro
