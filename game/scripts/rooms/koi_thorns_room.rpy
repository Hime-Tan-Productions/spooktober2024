label koi_thorns_room:
    scene bg koi_thorns
    
    if part == 2:
        if not int_koi_pond or not int_crown_of_thorns:
            menu:
                n "What should I do here?"
                "Ask Vivienne for an interview about the koi pond." if not int_koi_pond:
                    jump part2_viv_koi_pond_interview
                "Ask Vivienne for an interview about the crown of thorns." if not int_crown_of_thorns:
                    show vivienne neutral_folded_mouthopen
                    play vo "voices/Vivienne/what_do_you_want_2.mp3" noloop
                    n "I track down Vivienne."
                    jump part2_viv_crown_of_thorns_interview
                "Look around":
                    pass
    elif part == 3:
        jump koi_thorns_hide_choices
    call screen mansion_interior_koi_thorn

label koi_thorns_hide_choices:
    menu: 
        n "Where should I hide?"
        "In the koi pond":
            call suspicion(100, "death_hide_koi") from _call_suspicion_60
        "Among the crown of thorns.":
            call suspicion(100, "death_hide_cot") from _call_suspicion_61
        "Somewhere else.":
            call screen mansion_interior_koi_thorn
