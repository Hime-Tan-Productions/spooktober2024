label game_rps:
    menu:
        g "Let's play!"
        "Play":
            jump game_rps_play_start
        "How to play":
            jump game_rps_rules
        "What's my record?":
            jump game_rps_record
        "Other games":
            jump tutorial

label game_rps_rules:
    g "It's simple. Choose rock, paper, or scissors, and try to beat me!"
    jump game_rps

label game_rps_record:
    g "I don't know, was I supposed to be keeping track?"
    jump game_rps

label game_rps_play_start:
    g "Let's do this!"
    jump game_rps_play

label game_rps_play:
    $g_choice = renpy.random.choice(['r', 'p', 's'])
    menu:
        g "Rock. Paper. Scissors. SHOOT!"
        "Rock":
            $selection = "r"
        "Paper":
            $selection = "p"
        "Scissors":
            $selection = "s"

    if g_choice == selection:
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
    g "YES! I WIN! I AM THE GREATEST!"
    $rps_losses += 1
    jump game_rps

label game_rps_win:
    g "Ugh. You got lucky."
    $rps_wins += 1
    jump game_rps