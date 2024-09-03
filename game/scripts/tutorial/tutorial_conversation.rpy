label tutorial_conversation:
    scene bg_busstop
    show converso smile_2 at left
    menu:
        c "What shall we talk about?"
        "Tell me a story.":
            jump conv_story
        "What are you doing today?" if "converso bus" not in flags:
            jump conv_bus_1
        "Where are you taking the bus to?" if "converso bus" in flags and "converso far_away" not in flags:
            jump conv_bus_2
        "Why somewhere far away?" if "converso far_away" in flags and "converso why" not in flags:
            jump conv_bus_3
        "Why would Gabriella want to kill you?" if "converso why" in flags and "converso tell" not in flags:
            jump conv_bus_4
        "What's her tell?" if "converso tell" in flags:
            jump conv_bus_5
        "Back":
            hide converso
            jump tutorial


label conv_bus_1:
    "I'm waiting for the bus."
    $flags["converso bus"] = 1
    jump tutorial_conversation

label conv_bus_2:
    show converso surprised at left
    "Somewhere far away."
    $flags["converso far_away"] = 1
    jump tutorial_conversation

label conv_bus_3:
    show converso sad at left
    "Gabriella's gonna kill me."
    $flags["converso why"] = 1
    jump tutorial_conversation

label conv_bus_4:    
    show converso angry at left
    "I figured out her tell for one of her games."
    $flags["converso tell"] = 1
    jump tutorial_conversation

label conv_bus_5:
    show converso smile_3 at left
    "She gives away which hand she'll throw in rock paper scissors. Watch her face! Now quit asking about it - I've already said too much!"
    jump tutorial_conversation