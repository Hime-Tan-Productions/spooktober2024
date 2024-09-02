label conv_story:
    show converso smile_1
    if winning_streak >= 5:
        c "Whoa, you're really beating her! OK, here's a story..."
        jump conv_story_2
    else:
        c "Maybe once you've beat Gameria at a 3:1 ratio in one of her games."
        jump tutorial_conversation


label conv_story_2:
    show converso surprised
    c "In West Philadelphia born and raised"
    show converso smile_3
    c "On the playground is where I spent most of my days"
    show converso smile_2
    c "Chillin' out, maxin', relaxin' all cool"
    show converso smile_1
    c "And all shootin' some b-ball outside of the school"
    show converso surprised
    c "When a couple of guys who were up to no good"
    show converso sad
    c "Started makin' trouble in my neighborhood"
    show converso surprised
    c "I got in one little fight and my mom got scared"
    show converso angry
    c "And said \"You're movin' with your auntie and uncle in Bel-Air\""
    jump tutorial_conversation