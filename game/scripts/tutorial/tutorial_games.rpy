label tutorial_games:
    scene bg cave

    show Gameria happy

    g "Welcome to the game cave! What do you wanna play?"

    menu:
        "Flip a coin.":
            jump game_coin_flip
        "Rock paper scissors.":
            jump game_rps
        "Guess the number.":
            jump game_number_guess