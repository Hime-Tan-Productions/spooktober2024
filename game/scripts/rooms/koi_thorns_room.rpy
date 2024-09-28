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
    call screen mansion_interior_koi_thorn
