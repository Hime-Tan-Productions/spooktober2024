# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vivienne")
define s = Character("Stephanie")

# The game starts here.

label start:
    $playlist = [
        "moody progression (eerie wind chimes).mp3",
        "moody progression (halloween ambience).mp3",
        "moody progression (muted keys).mp3",
        "moody progression (mysterious tropics).mp3",
        "moody progression (mystic).mp3",
        "moody progression (uplifting moody keys).mp3",
        "moody progression (we have to hurry intensity).mp3",
        "moody progression (very dissonant and ghostly).mp3",
        "moody progression (ultra understated moody).mp3",
        "it was you (harsh horror reveal strings).mp3",
        "is someone behind me melody.mp3",
        "creepy wind chime melody.mp3",
        "reflective hip hoppy beat.mp3",
        "slow piano chords with some spooky ambience.mp3",
        "dubby maybe too upbeat investigative rhythm.mp3",
        "ghostly ethereal melody.mp3",
        "distant ambient keys.mp3",
        "ethereal watery ambient atmosphere.mp3",
        "garden trip hop esque groove with birds.mp3",
    ]
    $renpy.random.shuffle(playlist)

    play music playlist

    #scene bg room
    jump look_around


label look_around:
    call screen hidden_objects


label conv_vivienne:
    show vivienne conversation1
    v "I am Vivienne. Welcome to my greenhouse."
    show vivienne conversation2
    v "I'm a bad person."
    hide vivienne
    jump look_around


label conv_stephanie:
    show stephanie conversation
    s "I am Stephanie. I'm so nice!"
    s "You know you can trust me because I'm wearing big glasses."
    hide stephanie conversation
    jump look_around
