label corpse_plant_room:
    scene bg corpse_plant

    if "p2_corpse_plant_int" in flags.keys():
        menu:
            n "The viewing will begin soon. Are you ready?"
            "Yes":
                jump part3_start
            "No":
                pass

    call screen mansion_interior_corpse_plant
