label game_numberguess:
    show gameria smile at left

    menu:
        g "Let's play guess what number is behind my back!"
        "Play":
            jump game_numberguess_play_start
        "How to play":
            jump game_numberguess_rules
        "What's my record?":
            jump game_numberguess_record
        "Other games":
            jump tutorial_games

label game_numberguess_rules:
    g "Guess how many fingers I'm holding behind my back, 1 to 5. I won't cheat, I like super promise!"
    jump game_numberguess

label game_numberguess_record:
    if numberguess_wins == 0 and numberguess_losses == 0:
        show gameria smile at left
        g "We haven't played yet silly!"
    elif numberguess_wins == numberguess_losses:
        show gameria annoyed at left
        g "We're tied at [numberguess_wins]. For now..."
    elif numberguess_wins > numberguess_losses:
        show gameria annoyed at left
        g "Ugh. You're winning [numberguess_wins] to [numberguess_losses]. I guess."
    else:
        show gameria smug at left
        g "I'm up [numberguess_losses] to [numberguess_wins], naturally!"
    jump game_numberguess

label game_numberguess_play_start:
    jump game_numberguess_play

label game_numberguess_play:
    $number = renpy.random.randint(1, 5)

    $img = renpy.random.randint(1,3)
    if img == 1:
        show gameria smug at left
    elif img == 2:
        show gameria happy at left
    elif img == 3:
        show gameria smile at left
    menu:
        g "How many fingers am I holding up behind my back?"
        "1":
            $selection = 1
        "2":
            $selection = 2
        "3":
            $selection = 3
        "4":
            $selection = 4
        "5":
            $selection = 5
    if selection == number:
        jump game_numberguess_win
    else:
        jump game_numberguess_loss

label game_numberguess_loss:
    show gameria smug at left
    g "Gee, you're really bad at this one, aren't you? It was [number]."
    $numberguess_losses += 1
    jump game_numberguess

label game_numberguess_win:
    show gameria annoyed at left
    g "How are you so good at this?!"
    $numberguess_wins += 1
    jump game_numberguess