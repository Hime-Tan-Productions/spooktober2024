label death_crown_of_thorns:
    show vivienne angry
    $ renpy.music.set_volume(0.0,1.0,"music")
    $ renpy.sound.set_volume(0.0,0.0,"other")
    $ renpy.sound.set_volume(0.0,0.0,"noise")
    $ renpy.sound.set_volume(0.0,0.0,"sound")
    play death "it was you (harsh horror reveal strings).mp3" loop
    $ renpy.sound.set_volume(1.0,0.0,"death")
    $ renpy.music.set_volume(1.0,0.0,"sound")
    play sound "body impaled.mp3" noloop
    n "Vivienne swiftly pushes you into the plant and you experience firsthand how it feels to be penetrated by the world’s sharpest thorns."
    n "The plant’s roots eagerly drink up the blood spilling from your heart as Vivienne’s shrill laugh echoes throughout the greenhouse."
    $ renpy.sound.set_volume(0.0,0.1,"other")
    $ renpy.sound.set_volume(1.0,0.0,"noise")
    play sound "death gasp.mp3" noloop
    $ renpy.sound.set_volume(0.0,3.0,"death")
    $ renpy.music.set_volume(0.6,3.0,"music")
    play music "garden trip hop esque groove with birds.mp3" loop 