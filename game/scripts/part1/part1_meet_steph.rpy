label part1_meet_steph:
    $met_stephanie = True
    $ renpy.sound.set_volume(0.0,0.5,"other")
    show stephanie neutral_lookingdown
    pause
    p "Hello?"
    show stephanie scared
    s "Oh heavens! I didn't know someone else was here."
    p "Yes, Vivienne told me to come find you. I could barely see you hiding behind that tree!"
    show stephanie neutral_lookingdown_handsup
    s "It's a good place to hide from Vivienne."
    p "I didn't mean to frighten you, miss. I'm just here to ask some questions about the greenhouse."

    jump part1_steph_qs

label part1_steph_qs:
    show stephanie scared_handsup
    menu: 
        s "W-Why?"
        "The corpse flower is blooming.":
            jump steph_ask_greenhouse
        "The whole town seems to think there's something special here.":
            jump steph_ask_vivienne

label steph_ask_greenhouse:
    show stephanie neutral_lookingdown_handsup
    s "Yes. The whole town has come to see it. "
    p "Stephanie shifts her eyes left and right…"
    jump steph_nervous

label steph_ask_vivienne:
    show stephanie scared
    s "…"
    p "Stephanie shifts her eyes left and right…"
    show stephanie neutral_lookingdown_handsup
    s "Special? Um… well… Vivienne isn't your typical botanist… she… um… has her ways of doing things. "
    jump steph_nervous

label steph_nervous:
    show stephanie neutral_lookingdown
    menu:
        n "This poor girl seems rather nervous. She must be shy. Maybe I should just ask some easy questions for now."
        "What is the first thing you want readers to know about the corpse flower?":
            jump steph_ask_readers
        "What would you tell readers is so special about the greenhouse?":
            jump steph_ask_readers
        "What are you hiding?":
            jump steph_ask_hiding

label steph_ask_hiding:
    show stephanie scared
    s "I should get back to work!"
    jump part1_steph_end

label steph_ask_readers:
    show stephanie scared
    s "Readers?"
    p "Yes. I'm Asa Miller. I'm a reporter for The Greenville Gazette. Just trying to find out more about the plants from the people who know them best."
    show stephanie neutral_lookingup_handsup
    menu:
        s "Oh. I'm Stephanie. Stephanie Graham. I, um, thought you were investigating the plants for… other reasons."
        "Investigating? Did you think I was a detective?":
            jump steph_ask_detective
        "Like a rival gardener? I have killed far too many tomato plants to consider myself a green thumb.":
            jump steph_ask_gardener

label steph_ask_detective:
    show stephanie scared
    n "Stephanie nods."
    p "Haha! Well that might be the first time I've been mistaken as a police officer!"
    show stephanie neutral_lookingdown
    n "Stephanie laughs, but she still sounds nervous. Why would she think a detective would come here?"
    p "What is it like to work for Vivienne?"
    jump steph_ask_working

label steph_ask_gardener:
    show stephanie neutral_lookingdown
    n "Stephanie laughs, but she still sounds nervous."
    show stephanie neutral_lookingup
    p "What is it like to work for Vivienne?"
    jump steph_ask_working

label steph_ask_working:
    show stephanie neutral_lookingup_handsup
    menu:
        s "Vivienne does have her ways. But most of the time it's just me and the plants. I like it that way."
        "What do you mean by Vivienne having her ways?":
            jump steph_ask_ways
        "What is your favorite thing about the plants?":
            jump steph_ask_favorite

label steph_ask_ways:
    show stephanie scared
    s "Oh no! I didn't meant that. I think I've said too much."
    s "I have to get back to work."
    jump part1_steph_end

label steph_ask_favorite:
    show stephanie neutral_lookingup
    menu:
        s "They're just so calming. I love scent of all the blooms together. In the mornings I used to take a deep breath to take it all in. Of course, that's been ruined by…"
        "The scent of the new plant?":
            jump part1_steph_scent
        "The journalist interrupting your work?":
            jump part1_steph_journalist
        "Vivienne?":
            jump part1_steph_viv

label part1_steph_scent:
    show stephanie neutral_lookingdown_handsup
    s "Right."
    p "Guess I should go see the star of the show then."
    jump part1_steph_end

label part1_steph_journalist:
    show stephanie neutral_lookingdown_handsup
    s "I should get back to pruning these bushes. Got to have them looking nice for the guests tonight."
    jump part1_steph_end

label part1_steph_viv:
    show stephanie neutral_lookingdown_handsup
    s "I think you should go."
    jump part1_steph_end

label part1_steph_end:
    hide stephanie
    jump part2_start
