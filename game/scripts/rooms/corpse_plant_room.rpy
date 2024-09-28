label corpse_plant_room:

    if part != 3:
        scene bg corpse_plant
    else:
        scene bg corpse_plant_crowd

    if part == 2:
        if int_corpse_flower and int_banana_tree and int_koi_pond and int_crown_of_thorns and part2_stephanie_conv:
            menu:
                n "The viewing will begin soon. Are you ready?"
                "Yes.":
                    jump part3_start
                "No.":
                    pass

    call screen mansion_interior_corpse_plant
