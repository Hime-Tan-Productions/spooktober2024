label tutorial:
    show tutoriella_smile_2

    menu:
        t "Hello! What would you like to do?"
        "Talk with someone.":
            show tutoriella_smile_1
            t "My good friend Converso is always looking for someone to talk with!"
            jump tutorial_conversation
        "Play some games.":
            show tutoriella_smile_1
            t "You want to talk with Gameria. Don't let her trash talking get to you!"
            jump tutorial_games
        "Quit":
            $renpy.quit

    jump tutorial