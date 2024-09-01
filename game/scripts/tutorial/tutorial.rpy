label tutorial:
    show tutoriella happy

    menu:
        t "Hello! What would you like to do?"
        "Talk with you.":
            jump tutorial_conversation
        "Play some games.":
            jump tutorial_games
        "Quit":
            $renpy.quit

    jump tutorial