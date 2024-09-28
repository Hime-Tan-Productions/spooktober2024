label ending_walk_away:
    hide screen suspicion_bar with moveouttop
    scene black with fade
    stop sound
    stop music fadeout 0.5
    stop sound fadeout 0.5
    stop noise fadeout 0.5
    stop ambience fadeout 0.5
    stop other fadeout 0.5
    n "You make it back to the newsroom, but it is hard to write a good article."
    n "Without exploring the greenhouse more or asking Vivienne all of your questions, it is hard to write more than 300 words for the story."
    n "The editor in chief screams about how that's not enough to fill the front page and fires you immediately." 
    n "You dodge the typewriter as he throws it right at your head, but that's the end of your luck."
    n "With your reputation ruined, every job you apply for turns you down."
    n "You find yourself in line for bread at the soup kitchen, wishing you had explored the greenhouse further."
    call screen game_over
