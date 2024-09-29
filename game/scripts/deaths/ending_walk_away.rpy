label ending_walk_away:
    hide screen suspicion_bar with moveouttop
    scene black with fade
    $ renpy.music.set_volume(0.0,1.0,"music")
    $ renpy.sound.set_volume(0.0,1.0,"ambience")
    $ renpy.sound.set_volume(0.0,0.0,"other")
    $ renpy.sound.set_volume(0.0,0.0,"noise")
    $ renpy.sound.set_volume(0.0,0.0,"sound")
    play death "moody progression (very dissonant and ghostly).mp3" loop
    $ renpy.sound.set_volume(1.0,1.0,"sound")
    play sound "manual typerwriter.mp3" noloop
    n "You make it back to the newsroom, but it is hard to write a good article."
    n "Without exploring the greenhouse more or asking Vivienne all of your questions, it is hard to write more than 300 words for the story."
    n "The editor in chief screams about how that's not enough to fill the front page and fires you immediately." 
    $ renpy.sound.set_volume(0.0,1.0,"sound")
    $ renpy.sound.set_volume(1.0,0.0,"other")
    play other "typewriter throw.mp3" noloop
    n "You dodge the typewriter as he throws it right at your head, but that's the end of your luck."
    n "With your reputation ruined, every job you apply for turns you down."
    $ renpy.sound.set_volume(0.0,1.0,"sound")
    $ renpy.sound.set_volume(1.0,0.0,"ambience")
    play ambience "kitchen.mp3" noloop
    n "You find yourself in line for bread at the soup kitchen, wishing you had explored the greenhouse further."
    $ renpy.sound.set_volume(0.0,1.0,"ambience")
    $ renpy.sound.set_volume(0.0,3.0,"death")
    $ renpy.music.set_volume(0.6,3.0,"music")
    play music "garden trip hop esque groove with birds.mp3" loop 
    call screen game_over
