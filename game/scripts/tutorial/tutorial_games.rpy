label tutorial_games:
    scene bg_temple

    show gameria smile at left

    g "I AM THE GAME MASTER! TRY TO DEFEAT ME!"

    menu:
        "Flip a coin.":
            jump game_coinflip
        "Rock paper scissors.":
            jump game_rps
        "Guess the number.":
            jump game_numberguess
        "Start our win/loss record over" if coinflip_losses > 3 or numberguess_losses > 3 or rps_losses > 3:
            show gameria smug at left
            g "Embarrassed about all the losses you've racked up? You should be! Fine, we'll start over from the beginning."
            $rps_wins = 0
            $rps_losses = 0

            $coinflip_wins = 0
            $coinflip_losses = 0

            $numberguess_wins = 0
            $numberguess_losses = 0
            jump tutorial_games
        "That's all for now.":
            hide gameria
            jump tutorial