screen mansion_interior_koi_thorn():
    $left = False
    $right = False

    if part == 1:
        if met_vivienne:
            $left = True
    if part == 2:
        $left = True
        $right = True

    if left:
            imagebutton:
                xalign 0.1
                yalign 0.5
                idle "left"
                action [Stop("ambience", fadeout=2.0),Pause(1.0),Stop("other"),Stop("noise"),Jump("banana_room")]

    if right:
            imagebutton:
                xalign 0.9
                yalign 0.5
                idle "right"
                action [Stop("ambience", fadeout=2.0),Pause(1.0),Stop("other"),Stop("noise"),Play("sound","insect sounds 3.mp3"),Function(renpy.sound.set_volume, 0.6, channel="sound"),Jump("corpse_plant_room")]
    if part == 1:
        if not met_vivienne:
            imagebutton:
                xalign 0.5
                yalign 0
                idle "vivienne full_day"
                action Jump("part1_meet_viv")
    if part == 2:
        imagebutton:
            xalign 0.25
            yalign 0.75
            idle "watch"
            action Jump("part2_find_watch")
        imagebutton:
            xalign 0.25
            yalign 0.25
            idle "rosary"
            action Jump("part2_find_rosary")
        if not int_koi_pond:
            imagebutton:
                xalign 0.75
                yalign 0
                idle "vivienne full_day"
                action Jump("part2_viv_koi_pond_interview")
        elif not int_crown_of_thorns:
            imagebutton:
                xalign 0.75
                yalign 0
                idle "vivienne full_day"
                action Jump("part2_viv_crown_of_thorns_interview")
        elif int_corpse_flower and int_banana_tree:
            imagebutton:
                xalign 0.5
                yalign 0
                idle "stephanie full_day"
                action Jump("part2_stephanie_conv")