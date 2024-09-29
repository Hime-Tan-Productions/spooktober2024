label death_crown_of_thorns:
    show vivienne angry_folded
    $ renpy.music.set_volume(0.0,1.0,"music")
    $ renpy.sound.set_volume(0.0,0.0,"other")
    $ renpy.sound.set_volume(0.0,0.0,"noise")
    $ renpy.sound.set_volume(0.0,0.0,"sound")
    $ renpy.sound.set_volume(0.0,0.0,"nature")
    $ renpy.sound.set_volume(0.0,0.0,"ambience")
    play death "it was you (harsh horror reveal strings).mp3" loop
    $ renpy.sound.set_volume(1.0,0.0,"death")
    $ renpy.music.set_volume(1.0,0.0,"sound")
    play sound "body impaled.mp3" noloop
    n "Vivienne swiftly pushes you into the plant and you are penetrated by its thorns."
    n "Even in your dying thoughts, you still question whether they really are the world's sharpest."
    $ renpy.music.set_volume(0.9,0.0,"other")
    play other "vivienne laugh.mp3" noloop
    n "The plant's roots eagerly drink up the blood spilling from your heart as Vivienne's shrill laugh echoes throughout the greenhouse."
    $ renpy.sound.set_volume(0.0,0.1,"other")
    $ renpy.sound.set_volume(1.0,0.0,"noise")
    play sound "death gasp.mp3" noloop
    $ renpy.sound.set_volume(0.0,3.0,"death")
    $ renpy.music.set_volume(0.6,3.0,"music")
    $ renpy.sound.set_volume(0.0,4.0,"noise")
    play music "garden trip hop esque groove with birds.mp3" loop 
