label game_coinflip:
    show gameria_smile

    menu:
        g "Let's play flip the coin!"
        "Play":
            jump game_coinflip_play_start
        "How to play":
            jump game_coinflip_rules
        "What's my record?":
            jump game_coinflip_record
        "Other games":
            jump tutorial

label game_coinflip_rules:
    g "Call heads or tails while the coin is in the air!"
    jump game_coinflip

label game_coinflip_record:
    if coinflip_wins == 0 and coinflip_losses == 0:
        show gameria_smile
        g "We haven't played yet silly!"
    elif coinflip_wins == coinflip_losses:
        show gameria_annoyed
        g "We're tied at [coinflip_wins]. For now..."
    elif coinflip_wins > coinflip_losses:
        show gameria_annoyed
        g "Ugh. You're winning [coinflip_wins] to [coinflip_losses]. I guess."
    else:
        show gameria_smug
        g "I'm up [coinflip_losses] to [coinflip_wins], naturally!"
    jump game_coinflip

label game_coinflip_play_start:
    jump game_coinflip_play

label game_coinflip_play:
    $flip = renpy.random.choice(['h', 't'])
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
    show gameria_smug
    g "Skill issue."
    $coinflip_losses += 1
    jump game_coinflip

label game_coinflip_win:
    show gameria_annoyed
    g "Pure luck."
    $coinflip_wins += 1
    jump game_coinflip