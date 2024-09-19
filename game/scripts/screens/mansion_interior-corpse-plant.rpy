screen mansion_interior_corpse_plant():
    $left = False

    if part == 2:
        if "p2_viv_corpse_int" in flags.keys():
            $left = True        
        else:
            imagebutton:
                xalign 0.5
                yalign 0
                idle "vivienne full"
                action Jump("part2_viv_corpse_plant_interview")

    if left:
        imagebutton:
            xalign 0.1
            yalign 0.5
            idle "left"
            action Jump("part1_main")