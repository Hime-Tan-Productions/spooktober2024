# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vivienne")
define s = Character("Stephanie")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    jump repeat_menu


label repeat_menu:
    menu:
        "Who should I approach?"
    
        "Stephanie":
            jump conv_stephanie
    
        "Vivienne":    
            jump conv_vivienne


label conv_vivienne:
    show vivienne_conversation
    v "I am Vivienne. Welcome to my greenhouse."
    v "I'm a bad person."
    hide vivienne_conversation
    jump repeat_menu


label conv_stephanie:
    show stephanie_conversation
    s "I am Stephanie. I'm so nice!."
    s "You know you can trust me because I'm wearing big glasses."
    hide stephanie_conversation
    jump repeat_menu
