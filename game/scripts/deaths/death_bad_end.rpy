label death_bad_end:
    $ renpy.music.set_volume(0.0,1.0,"music")
    $ renpy.sound.set_volume(0.0,0.0,"other")
    $ renpy.sound.set_volume(0.0,0.0,"noise")
    $ renpy.sound.set_volume(0.0,0.0,"sound")
    play death "it was you (harsh horror reveal strings).mp3" loop
    $ renpy.sound.set_volume(1.0,0.0,"death")
    n "You become the fifth sacirfice to the corpse flower."
    $ renpy.sound.set_volume(1.0,0.0,"sound")
    play sound "eaten by plant.mp3" noloop
    n "Its sharp teeth shred your body to bits and gulp down what's left of you." 
    n "There is no trace left of your murder and you are posthumously fired for missing your deadline."
    $ renpy.music.set_volume(0.9,0.0,"other")
    play other "death gasp.mp3" noloop
    $ renpy.sound.set_volume(0.0,3.0,"death")
    $ renpy.music.set_volume(0.6,3.0,"music")
    play music "garden trip hop esque groove with birds.mp3" loop 
