label tutorial:
    show tutoriella  smile_2

    menu:
        t "Hello! What would you like to do?"
        "Talk with someone.":
            show tutoriella  smile_1
            t "My good friend Converso is always looking for someone to talk with!"
            hide tutoriella
            jump tutorial_conversation
        "Play some games.":
            show tutoriella  smile_1
            t "You want to talk with Gameria. Don't let her trash talking get to you!"
            hide tutoriella
            jump tutorial_games
        "Quit":
            $renpy.quit

    jump tutorial