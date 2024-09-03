label tutorial:
    show tutoriella  smile_2 at left

    menu:
        t "Find someone else to bother please."
        "Is there anyone here to talk to?":
            show tutoriella  smile_1 at left
            t "Converso always has the best stories. Here, I'll call him over!"
            hide tutoriella
            jump tutorial_conversation
        "I just want to play some games.":
            show tutoriella  smile_1 at left
            t "Gameria is your girl. HEY GAMERIA!"
            hide tutoriella
            jump tutorial_games
        "Quit":
            $renpy.quit

    jump tutorial