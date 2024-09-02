label game_rps:
    show gameria  smile

    menu:
        g "Let's play rock paper scissors!"
        "Play":
            jump game_rps_play_start
        "How to play":
            jump game_rps_rules
        "Other games":
            jump tutorial_games

label game_rps_rules:
    g "It's simple. Choose rock, paper, or scissors, and try to beat me!"
    jump game_rps

label game_rps_play_start:
    jump game_rps_play

label game_rps_play:
    $g_choice = renpy.random.choice(['r', 'p', 's'])
    if g_choice == "r":
        show gameria smile at left
    elif g_choice == "p":
        show gameria happy at left
    elif g_choice == "s":
        show gameria smug at left
    menu:
        g "Rock. Paper. Scissors. SHOOT!"
        "Rock":
            $selection = "r"
        "Paper":
            $selection = "p"
        "Scissors":
            $selection = "s"

    if g_choice == selection:
        show gameria  smile
        g "A tie! Let's go again!"
        jump game_rps_play

    if selection == "r":
        if g_choice == "p":
            jump game_rps_loss
        else:
            jump game_rps_win
    if selection == "p":
        if g_choice == "s":
            jump game_rps_loss
        else:
            jump game_rps_win
    if selection == "s":
        if g_choice == "r":
            jump game_rps_loss
        else:
            jump game_rps_win

label game_rps_loss:
    show gameria happy at left
    g "YES! I WIN! I AM THE GREATEST!"
    $winning_streak = 0
    jump game_rps

label game_rps_win:
    show gameria annoyed at left
    g "Ugh. You got lucky."
    $winning_streak += 1
    jump game_rps