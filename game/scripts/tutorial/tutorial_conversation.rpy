label tutorial_conversation:
    scene bg_busstop
    show converso smile_2 at left
    menu:
        c "Sup?"
        "Tell me a story.":
            jump conv_story
        "What are you doing today?" if bus_story_index == 0:
            jump conv_bus_1
        "Where are you taking the bus to?" if bus_story_index == 1:
            jump conv_bus_2
        "Why somewhere far away?" if bus_story_index == 2:
            jump conv_bus_3
        "Why would Gameria want to kill you?" if bus_story_index == 3:
            jump conv_bus_4
        "What's her tell?" if bus_story_index == 4:
            jump conv_bus_5
        "Back":
            hide converso
            jump tutorial


label conv_bus_1:
    "I'm waiting for the bus."
    $bus_story_index = 1
    jump tutorial_conversation

label conv_bus_2:
    show converso surprised at left
    "Somewhere far away."
    $bus_story_index = 2
    jump tutorial_conversation

label conv_bus_3:
    show converso sad at left
    "Gameria's gonna kill me."
    $bus_story_index = 3
    jump tutorial_conversation

label conv_bus_4:    
    show converso angry at left
    "I figured out her tell for one of her games."
    $bus_story_index = 4
    jump tutorial_conversation

label conv_bus_5:
    show converso smile_3 at left
    "She gives away which hand she'll throw in rock paper scissors. Watch her face! Now quit asking about it - I've already said too much!"
    jump tutorial_conversation