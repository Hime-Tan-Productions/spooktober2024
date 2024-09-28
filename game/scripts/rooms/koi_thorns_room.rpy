label koi_thorns_room:
    scene bg koi_thorns
    
    if part == 2:
        if not int_koi_pond or not int_crown_of_thorns:
            menu:
                n "What should I do here?"
                "Ask Vivienne for an interview about the koi pond." if not int_koi_pond:
                    jump part2_viv_koi_pond_interview
                "Ask Vivienne for an interview about the crown of thorns." if not int_crown_of_thorns:
                    n "I track down Vivienne."
                    jump part2_viv_crown_of_thorns_interview
                "Look around":
                    pass
    elif part == 3 and not saw_koi_thorns_hide_choices:
        $choices = []
        jump koi_thorns_hide_choices
    call screen mansion_interior_koi_thorn

label koi_thorns_hide_choices:
    menu: 
        set choices
        n "Where should I hide?"
        "In the koi pond":
            p "Am I crazy? I'll pass out from the smell!"
            jump koi_thorns_hide_choices
        "Among the crown of thorns.":
            p "My clothes will get wet!"
            jump koi_thorns_hide_choices
        "Somewhere else.":
            $saw_koi_thorns_hide_choices = True
            jump koi_thorns_room
