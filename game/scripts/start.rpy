# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character(name=None, color="#ffd73a", what_italic = True)
define p = Character(name="Asa", color="#ffd73a")
define v = Character("Vivienne", color="#ffd73a")
define s = Character("Stephanie", color="#ffd73a")
define moreno = Character("Moreno", color="#ffd73a")
define nun = Character("Sister Garcia", color="#ffd73a")
define howard = Character("Vivienne's Husband", color="#ffd73a")

label start:

# variables
    $journal_people = []
    $journal_story = []
    $journal_todo = []
    $part = 0
    $suspicion = 0
    $max_suspicion = 100
# flags
    $met_vivienne = False
    $met_stephanie = False

    $part2_stephanie_conv = False

    $int_corpse_flower = False
    $int_crown_of_thorns = False
    $int_koi_pond = False
    $int_banana_tree = False

    $clue_moreno = False
    $clue_stephanie = False
    $clue_nun = False
    $clue_howard = False

    $saw_koi_thorns_hide_choices = False

    # if debug sus controls are needed
    show screen debug_screen

    scene black with fade
    #show screen journal_tabs with moveinleft
    show screen suspicion_bar with moveintop
    jump outline_example
    jump intro
