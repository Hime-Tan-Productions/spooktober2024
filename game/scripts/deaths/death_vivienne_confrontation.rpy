label death_vivienne_confrontation:
    $ renpy.music.set_volume(0.0,1.0,"music")
    $ renpy.sound.set_volume(0.0,0.0,"other")
    $ renpy.sound.set_volume(0.0,0.0,"noise")
    $ renpy.sound.set_volume(0.0,0.0,"sound")
    $ renpy.music.set_volume(0.0,1.0,"ambience")
    play death "it was you (harsh horror reveal strings).mp3" loop
    $ renpy.sound.set_volume(1.0,0.0,"death")
    $ renpy.music.set_volume(1.0,0.0,"sound")
    n "I go seek out Vivienne."
    $ renpy.music.set_volume(1.0,0.0,"sound")
    play sound "sword-drawing.mp3" noloop
    n "But she finds me first."
    $ renpy.music.set_volume(0.9,0.0,"nature")
    play nature "stab sound 2.mp3" noloop
    n "I feel the cold steel of her garden sheers slip into my back."
    v "I've had quite enough of your questions."
    v "You'll no longer be writing this story."
    v "You'll be part of it."
    play nature "stab sound 2.mp3" noloop
    $ renpy.music.set_volume(0.9,0.0,"other")
    play other "death gasp.mp3" noloop
    $ renpy.sound.set_volume(0.0,3.0,"death")
    $ renpy.music.set_volume(0.6,3.0,"music")
    play music "garden trip hop esque groove with birds.mp3" loop 

