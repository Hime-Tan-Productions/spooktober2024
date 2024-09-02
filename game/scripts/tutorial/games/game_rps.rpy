label game_rps:
    show gameria  smile

    menu:
        g "Let's play rock paper scissors!"
        "Play":
            jump game_rps_play_start
        "How to play":
            jump game_rps_rules
        "What's my record?":
            jump game_rps_record
        "Other games":
            jump tutorial_games

label game_rps_rules:
    g "It's simple. Choose rock, paper, or scissors, and try to beat me!"
    jump game_rps

label game_rps_record:
    if rps_wins == 0 and rps_losses == 0:
        show gameria  smile
        g "We haven't played yet silly!"
    elif rps_wins == rps_losses:
        show gameria  annoyed
        g "We're tied at [rps_wins]. For now..."
    elif rps_wins > rps_losses:
        show gameria  annoyed
        g "Ugh. You're winning [rps_wins] to [rps_losses]. I guess."
    else:
        show gameria  smug
        g "I'm up [rps_losses] to [rps_wins], naturally!"
    jump game_rps

label game_rps_play_start:
    jump game_rps_play

label game_rps_play:
    $g_choice = renpy.random.choice(['r', 'p', 's'])
    if g_choice == "r":
        show gameria smile
    elif g_choice == "p":
        show gameria happy
    elif g_choice == "s":
        show gameria smug
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
    show gameria  happy
    g "YES! I WIN! I AM THE GREATEST!"
    $rps_losses += 1
    jump game_rps

label game_rps_win:
    show gameria  annoyed
    g "Ugh. You got lucky."
    $rps_wins += 1
    jump game_rps