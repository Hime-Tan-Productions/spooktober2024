label part2_moreno:
    show vivienne angry_folded
    p "I'm sorry if I ask basic questions, Vivienne."
    p "You see, I'm not the first reporter from The Greenville Gazette to cover this story."
    p "Did my colleague Moreno contact you?"
    show vivienne angry_armup
    play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop
    menu:
        v "I've never heard such a name!"
        "His pocket watch is in your koi pond.":
            $ renpy.music.set_volume(0.0,1.0,"music")
            $ renpy.sound.set_volume(0.0,0.0,"other")
            $ renpy.sound.set_volume(0.0,0.0,"noise")
            $ renpy.sound.set_volume(0.0,0.0,"sound")
            play death "it was you (harsh horror reveal strings).mp3" loop
            $ renpy.sound.set_volume(1.0,0.0,"death")
            call suspicion(100, "death_koi_pond") from _call_suspicion_44
        "Are you sure?":
            $ renpy.music.set_volume(0.0,1.0,"music")
            $ renpy.sound.set_volume(0.0,0.0,"other")
            $ renpy.sound.set_volume(0.0,0.0,"noise")
            $ renpy.sound.set_volume(0.0,0.0,"sound")
            play death "it was you (harsh horror reveal strings).mp3" loop
            $ renpy.sound.set_volume(1.0,0.0,"death")
            call suspicion(100, "death_koi_pond") from _call_suspicion_45
            call suspicion(100, "death_koi_pond") from _call_suspicion_46
