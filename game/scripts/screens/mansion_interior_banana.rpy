screen mansion_interior_banana():
    $right = False

    if part == 1 or part == 2:
        $right = True

    if right:
        imagebutton:
            xalign 0.9
            yalign 0.5
            idle "right"
            action Jump("part1_main")
    if part == 1:
        if not met_stephanie:
            imagebutton:
                xalign 0.5
                yalign 0.5
                idle "hat"
                action Jump("part1_meet_steph")
    elif part == 2:
        imagebutton:
            xalign 0.4
            yalign 0.4
            idle "bottle"
            action Jump("part2_found_bottle")
        if not int_banana_tree:
            imagebutton:
                xalign 0.75
                yalign 0
                idle "vivienne full"
                action Jump("part2_viv_banana_tree_interview")