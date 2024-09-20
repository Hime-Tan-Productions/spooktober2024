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
        imagebutton:
            xalign 0.5
            yalign 0
            idle "stephanie full"
            action Jump("part1_meet_steph")
    elif part == 2:
        if "p2_viv_banana_tree_int" not in flags.keys():
            imagebutton:
                xalign 0.5
                yalign 0
                idle "vivienne full"
                action Jump("part2_viv_banana_tree_interview")