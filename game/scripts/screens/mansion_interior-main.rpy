screen mansion_interior_main():
    if "met_vivienne" in flags.keys():
        imagebutton:
            xalign 0.1
            yalign 0.5
            idle "left"
            action Jump("part1_left")
        imagebutton:
            xalign 0.9
            yalign 0.5
            idle "right"
            action Jump("part1_right")
    imagebutton:
        xalign 0.5
        yalign 0
        idle "vivienne full"
        action Jump("part1_meet_viv")