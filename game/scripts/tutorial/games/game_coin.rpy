label game_coinflip:
    show gameria smile at left

    menu:
        g "Let's play flip the coin!"
        "Play":
            jump game_coinflip_play_start
        "How to play":
            jump game_coinflip_rules
        "What's my winning streak?":
            jump game_coinflip_record
        "Other games":
            jump tutorial_games

label game_coinflip_rules:
    g "Call heads or tails while the coin is in the air!"
    jump game_coinflip

label game_coinflip_record:
    if winning_streak == 0 and winning_streak == 0:
        show gameria smile at left
        g "Currently... 0"
    elif winning_streak > 0:
        show gameria annoyed at left
        g "Ugh. Your winning streak is [winning_streak]."
    else:
        show gameria smug
        g "Who knows!"
    jump game_coinflip


label game_coinflip_play_start:
    jump game_coinflip_play

label game_coinflip_play:
    $flip = renpy.random.choice(['h', 't'])
    $img = renpy.random.randint(1,3)
    if img == 1:
        show gameria smug at left
    elif img == 2:
        show gameria happy at left
    elif img == 3:
        show gameria smile at left

    menu:
        g "Call it in the air!"
        "Heads":
            $selection = "h"
        "Tails":
            $selection = "t"

    if flip == 'h':
        g "Heads."
    else:
        g "Tails."

    if selection == flip:
        jump game_coinflip_win
    else:
        jump game_coinflip_loss

label game_coinflip_loss:
    show gameria smug at left
    g "Skill issue."
    $winning_streak = 0
    jump game_coinflip

label game_coinflip_win:
    show gameria annoyed at left
    g "Pure luck."
    $winning_streak += 1
    jump game_coinflip