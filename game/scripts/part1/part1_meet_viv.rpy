label part1_meet_viv:
    show vivienne neutral_armup
    pause
    if not met_vivienne:
        $met_vivienne = True
    else:
        jump part1_viv_see_flower
    "As a reporter, I have to keep my sources happy so that they'll open up to me."
    "Asking the wrong questions could make them not want to speak to me any further."
    show vivienne angry_armup
    p "Hi! I'm here with The Greenville Gazette to cover your corpse flower bloom. It's nice to meet you!"
    n "You hold out your hand to shake Vivienne's but she does not return the gesture."
    jump part1_viv_qs

label part1_viv_qs:
    show vivienne angry_folded
    play vo "voices/Vivienne/viv_4_yoshi_distain.mp3"
    menu:
        v "You're here too early for the bloom. Doors open to the public at 6 p.m."
        "Right. I thought I could ask you some questions about the flower beforehand!":
            jump part1_viv_flower_questions
        "I know, but I just couldn't wait to see the flower!":
            jump part1_viv_couldnt_wait

label part1_viv_flower_questions:
    call suspicion(20, "death_corpse_plant")
    menu:
        v "Why would you do such a thing! Don't you know it's rude to show up unannounced?"
        "I'm sorry. I know this time is difficult for you. I'm sorry to hear about your husband.":
            show vivienne angry_armup
            call suspicion(25, "death_corpse_plant")
            v "What about my husband? Would you be asking me these questions if I were a man? My plants bloom better than ever with him gone!"
            jump part1_viv_see_flower
        "I would have called earlier, but my boss cut the phone cord when he was angry.":
            jump part1_viv_laugh

label part1_viv_laugh:
    show vivienne happy_folded
    menu:
        v "Hahaha! What a fabulous idea!"
        "Laugh with her":
            call suspicion(-10)
            jump part1_viv_see_flower
        "Don't laugh":
            call suspicion(25, "death_corpse_plant")
            jump part1_viv_see_flower

label part1_viv_couldnt_wait:
    jump part1_viv_see_flower

label part1_viv_see_flower:
    show vivienne angry_armup
    v "You couldn't have come at a worse time. I have so much to prepare for tonight!"
    v "Stephanie! Stephanie! Where's that lazy girl when you need her?"
    "Go find my good-for-nothing employee and she will show you around until I'm ready."
    jump part1_viv_end

label part1_viv_end:
    hide vivienne
    jump part1_main
