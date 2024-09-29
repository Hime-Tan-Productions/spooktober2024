label death_hide_cot:
    hide vivienne
    $ renpy.music.set_volume(0.0,1.0,"music")
    $ renpy.sound.set_volume(0.0,0.0,"other")
    $ renpy.sound.set_volume(0.0,0.0,"noise")
    $ renpy.sound.set_volume(0.0,0.0,"sound")
    $ renpy.sound.set_volume(0.0,1.0,"ambience")
    play death "it was you (harsh horror reveal strings).mp3" loop
    $ renpy.sound.set_volume(1.0,0.0,"death")
    $ renpy.music.set_volume(1.0,0.0,"sound")
    n "Hiding in a thorny plant is the worst idea you've ever had."
    play sound "body impaled.mp3" noloop
    n "What are quite possibly the world's sharpest thorns pierce through every major organ in your body as your hiding place becomes your final resting place."
    $ renpy.sound.set_volume(0.0,0.1,"other")
    $ renpy.sound.set_volume(1.0,0.0,"noise")
    play sound "death gasp.mp3" noloop
    $ renpy.sound.set_volume(0.0,3.0,"death")
    $ renpy.music.set_volume(0.6,3.0,"music")
    $ renpy.music.set_volume(0.0,4.0,"noise")
    play music "garden trip hop esque groove with birds.mp3" loop 