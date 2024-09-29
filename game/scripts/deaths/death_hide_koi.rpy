label death_hide_koi:
    hide vivienne
    $ renpy.music.set_volume(0.0,1.0,"music")
    $ renpy.sound.set_volume(0.0,0.0,"other")
    $ renpy.sound.set_volume(0.0,0.0,"noise")
    $ renpy.sound.set_volume(0.0,0.0,"sound")
    play death "it was you (harsh horror reveal strings).mp3" loop
    $ renpy.sound.set_volume(1.0,0.0,"death")
    $ renpy.music.set_volume(1.0,0.0,"sound")
    play sound "drowning.mp3" noloop
    n "As you dive into the koi pond, you discover that Vivienne wasn't fibbing about her koi pond being extra special."
    n "The koi rush at you with their razor-sharp teeth and tear apart your flesh."
    show vivienne angry_folded
    n "Your blood fills the koi pond as Vivienne watches in glee nearby."
    $ renpy.sound.set_volume(0.0,3.0,"death")
    $ renpy.sound.set_volume(0.0,3.0,"sound")
    $ renpy.music.set_volume(0.6,3.0,"music")
    $ renpy.music.set_volume(0.0,4.0,"sound")
    play music "garden trip hop esque groove with birds.mp3" loop 
