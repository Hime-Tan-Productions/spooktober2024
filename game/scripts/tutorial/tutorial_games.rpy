label tutorial_games:
    scene bg_temple

    show gameria_smile

    g "Welcome to the game area! What do you wanna play?"

    menu:
        "Flip a coin.":
            jump game_coinflip
        "Rock paper scissors.":
            jump game_rps
        "Guess the number.":
            jump game_numberguess
        "That's all for now.":
            jump tutorial