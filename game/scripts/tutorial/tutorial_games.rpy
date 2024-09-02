label tutorial_games:
    scene bg_temple

    show gameria smile at left

    g "Welcome to the game area! What do you wanna play?"

    menu:
        "Flip a coin.":
            jump game_coinflip
        "Rock paper scissors.":
            jump game_rps
        "Guess the number.":
            jump game_numberguess
        "That's all for now.":
            hide gameria
            jump tutorial