label corpse_plant_room:
    scene bg corpse_plant

    if int_corpse_flower:
        menu:
            n "The viewing will begin soon. Are you ready?"
            "Yes":
                jump part3_start
            "No":
                pass

    call screen mansion_interior_corpse_plant
