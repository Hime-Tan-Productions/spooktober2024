screen mansion_interior_koi_thorn():
    $left = False
    $right = False

    if part == 1:
        if "met_vivienne" in flags.keys():
            $left = True
    if part == 2:
        $left = True
        $right = True

    if left:
            imagebutton:
                xalign 0.1
                yalign 0.5
                idle "left"
                action Jump("banana_room")
    if right:
            imagebutton:
                xalign 0.9
                yalign 0.5
                idle "right"
                action Jump("corpse_plant_room")
    if part == 1:
        imagebutton:
            xalign 0.5
            yalign 0
            idle "vivienne full"
            action Jump("part1_meet_viv")
    if part == 2:
        imagebutton:
            xalign 0.25
            yalign 0.25
            idle "watch"
            action Jump("part2_find_watch")
        imagebutton:
            xalign 0.25
            yalign 0.75
            idle "rosary"
            action Jump("part2_find_rosary")
        if "p2_viv_koi_pond_int" not in flags.keys():
            imagebutton:
                xalign 0.75
                yalign 0
                idle "vivienne full"
                action Jump("part2_viv_koi_pond_interview")
        elif "p2_viv_crown_of_thorns_int" not in flags.keys():
            imagebutton:
                xalign 0.75
                yalign 0
                idle "vivienne full"
                action Jump("part2_viv_crown_of_thorns_interview")
        elif "p2_viv_corpse_plant_int" in flags.keys() and "p2_viv_banana_tree_int" in flags.keys():
            imagebutton:
                xalign 0.5
                yalign 0
                idle "stephanie full"
                action Jump("part2_stephanie_conv")