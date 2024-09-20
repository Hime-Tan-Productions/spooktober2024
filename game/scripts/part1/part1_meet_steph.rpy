label part1_meet_steph:
    $flags["met_stephanie"] = True
    show stephanie conversation
    pause
    p "I didn’t mean to frighten you, miss. I’m just here to ask some questions about the greenhouse."
    p "Excuse me!"
    u "Oh hello there! My name is Stephanie."
    p "I didn’t mean to frighten you, miss. I’m just here to ask some questions about the greenhouse."
    jump part1_steph_qs

label part1_steph_qs:
    menu: 
        s "W-Why?"
        "The corpse flower is blooming.":
            jump steph_ask_greenhouse
        "What do you think makes the corpse flower so special?":
            jump steph_ask_vivienne
        "That's all.":
            hide stephanie
            jump part1_left

label steph_ask_greenhouse:
    p "The corpse flower is blooming."
    s "Yes. The whole town has come to see it. "
    p "Stephanie shifts her eyes left and right..."
    jump steph_nervous

label steph_ask_vivienne:
    p "What do you think makes the corpse flower so special?"
    show stephanie scared
    s "..."
    p "Stephanie shifts her eyes left and right..."
    show stephanie conversation
    s "Special? Um…well…Vivienne isn’t your typical botanist…she..um…has her ways of doing things. "
    jump steph_nervous

label steph_nervous:
    menu:
        n "This poor girl seems rather nervous. She must be shy. Maybe I should just ask some easy questions for now."
        "What is the first thing you want readers to know about the corpse flower?":
            s "Readers?"
            p "Yes. I’m <player name>. I’m a reporter for The Eyewitness. Just trying to find out more about the plants from the people who know them best."
            jump steph_ask_readers
        "What would you tell readers is so special about the greenhouse?":
            s "Readers?"
            p "Yes. I’m <player name>. I’m a reporter for The Eyewitness. Just trying to find out more about the plants from the people who know them best."
            jump steph_ask_readers
        "What are you hiding?":
            jump steph_ask_hiding

label steph_ask_hiding:
    s "I should get back to work!"
    jump part1_steph_end

label steph_ask_readers:
    menu:
        s "Oh. I’m Stephanie. Stephanie Graham. I, um, thought you were investigating the plants for…other reasons."
        "Investigating? Did you think I was a detective?":
            jump steph_ask_detective
        "Like a rival gardener? I hate to diappoint you, Miss Graham, but I have killed far too many tomato plants to consider myself a plant person.":
            jump steph_ask_gardener

label steph_ask_detective:
    n "Stephanie nods."
    p "Haha! Well that might be the first time I’ve been mistaken as a police officer!"
    n "Stephanie laughs, but she still sounds nervous. Why would she think a detective would come here?"
    p "What is it like to work for Vivienne?"
    jump steph_ask_working

label steph_ask_gardener:
    n "Stephanie laughs, but she still sounds nervous."
    p "What is it like to work for Vivienne?"
    jump steph_ask_working

label steph_ask_working:
    menu:
        s "Vivienne does have her ways. But most of the time it’s just me and the plants. I like it that way."
        "What do you mean by Vivienne’s having her ways?":
            jump steph_ask_ways
        "What is your favorite thing about the plants?":
            jump steph_ask_favorite

label steph_ask_ways:
    s "Oh no! I didn’t meant that. I think I’ve said too much."
    s "I have to get back to work."
    jump part1_steph_end

label steph_ask_favorite:
    menu:
        s "They’re just so calming. I love scent of all the blooms together. In the mornings I used to take a deep breath to take it all in. Of course, that’s been ruined by…"
        "The scent of the new plant?":
            jump part1_steph_scent
        "The journalist interrupting your work?":
            jump part1_steph_journalist
        "Vivienne?":
            jump part1_steph_viv

label part1_steph_scent:
    s "Right."
    p "Guess I should go see the star of the show then."
    jump part1_steph_end

label part1_steph_journalist:
    s "I should get back to pruning these bushes. Got to have them looking nice for the guests tonight."
    jump part1_steph_end

label part1_steph_viv:
    s "I think you should go."
    jump part1_steph_end

label part1_steph_end:
    hide stephanie
    jump part1_main



