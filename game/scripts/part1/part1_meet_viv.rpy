label part1_meet_viv:
    show vivienne conversation
    pause
    if "met_vivienne" not in flags:
        $flags["met_vivienne"] = 1
    else:
        jump part1_viv_see_flower    
    p "Hi! I’m here with The Eyewitness to cover your corpse flower bloom. It’s nice to meet you!"
    n "You hold out your hand to shake Vivienne’s but she does not return the gesture."
    jump part1_viv_qs

label part1_viv_qs:
    menu:
        v "You’re here too early for the bloom. Doors open to the public at 6 p.m."
        "Right. I thought I could ask you some questions about the flower beforehand!":
            jump part1_viv_flower_questions
        "I know, but I just couldn’t wait to see the flower!":
            jump part1_viv_couldnt_wait

label part1_viv_flower_questions:
    call suspicion(20)
    menu:
        v "Why would you do such a thing! Don’t you know it’s rude to show up unannounced?"
        "I’m sorry. I know this time is difficult for you. I’m sorry to hear about your husband.":
            call suspicion(25)
            v "What about my husband? Would you be asking me these questions if I were a man? My plants bloom better than ever with him gone!"
            jump part1_viv_see_flower
        "I would have called earlier, but my boss cut the phone cord when he was angry":
            jump part1_viv_laugh

label part1_viv_laugh:
    menu:
        v "Hahaha! What a fabulous idea!"
        "Laugh with her":
            call suspicion(-10)
            jump part1_viv_see_flower
        "Don't laugh":
            call suspicion(10)
            jump part1_viv_see_flower

label part1_viv_couldnt_wait:
    jump part1_viv_see_flower

label part1_viv_see_flower:
    menu:
        v "I suppose a sneak peek for the press is good for business."
        "Yes":
            v "She's right this way."
            jump part1_corpse_flower
        "Maybe later":
            v "Tell me when you're ready."
            jump part1_viv_end

label part1_viv_end:
    hide vivienne
    jump part1_main
