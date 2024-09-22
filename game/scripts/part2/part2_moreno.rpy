label part2_moreno:
    p "I'm sorry if I ask basic questions, Vivienne."
    p "You see, I’m not the first reporter from The Eyewitness to cover this story."
    p "Did my colleague Moreno contact you?"
    menu:
        v "I've never heard such a name!"
        "His pocket watch is in your koi pond.":
            $ renpy.music.set_volume(0.0,1.0,"music")
            $ renpy.sound.set_volume(0.0,0.0,"other")
            $ renpy.sound.set_volume(0.0,0.0,"noise")
            $ renpy.sound.set_volume(0.0,0.0,"sound")
            play death "it was you (harsh horror reveal strings).mp3" loop
            $ renpy.sound.set_volume(1.0,0.0,"death")
            call suspicion(100, "death_koi_pond")
        "Are you sure?":
            $ renpy.music.set_volume(0.0,1.0,"music")
            $ renpy.sound.set_volume(0.0,0.0,"other")
            $ renpy.sound.set_volume(0.0,0.0,"noise")
            $ renpy.sound.set_volume(0.0,0.0,"sound")
            play death "it was you (harsh horror reveal strings).mp3" loop
            $ renpy.sound.set_volume(1.0,0.0,"death")
            call suspicion(100, "death_koi_pond")
            call suspicion(100, "death_koi_pond")
