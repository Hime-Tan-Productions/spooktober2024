label death_banana:
    show vivienne angry_folded

    $ renpy.music.set_volume(0.0,1.0,"music")
    $ renpy.sound.set_volume(0.0,0.0,"other")
    $ renpy.sound.set_volume(0.0,0.0,"noise")
    $ renpy.sound.set_volume(0.0,0.0,"sound")
    play death "it was you (harsh horror reveal strings).mp3" loop
    $ renpy.sound.set_volume(1.0,0.0,"death")

    v "Why don't you try one of the bananas? They're wonderful!"
    menu:
        "I don't like bananas.":
            v "Unfortunately, you don't have a choice."
            jump death_banana_cont
        "I'd love to!":
            v "More food for my sweet girl."
            jump death_banana_cont


label death_banana_cont:
    $ renpy.sound.set_volume(1.0,0.0,"sound")
    play sound "gulp.mp3" noloop
    n "Vivienne shoves a poisoned banana in your mouth. As you swallow the sweet fruit, your throat quickly asphyxiates."
    $ renpy.sound.set_volume(1.0,0.0,"other")
    stop sound
    play other "gagging.mp3"
    n "The potassium from the banana does not prevent muscle cramps as your body seizures until it never moves again."
    $ renpy.sound.set_volume(0.0,0.1,"other")
    $ renpy.sound.set_volume(1.0,0.0,"noise")
    play sound "death gasp.mp3" noloop
    $ renpy.sound.set_volume(0.0,3.0,"death")
    $ renpy.music.set_volume(0.6,3.0,"music")
    $ renpy.sound.set_volume(0.0,4.0,"noise")
    play music "garden trip hop esque groove with birds.mp3" loop 
