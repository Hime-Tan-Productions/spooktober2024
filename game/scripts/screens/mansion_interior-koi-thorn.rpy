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
                action Jump("part1_left")
    if right:
            imagebutton:
                xalign 0.9
                yalign 0.5
                idle "right"
                action Jump("part1_right")
    if part == 1:
        imagebutton:
            xalign 0.5
            yalign 0
            idle "vivienne full"
            action Jump("part1_meet_viv")