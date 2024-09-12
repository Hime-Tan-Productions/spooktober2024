screen mansion_interior_main():
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
    if "explored_left" in flags.keys() and "explored_right" in flags.keys():
        imagebutton:
            xalign 0.5
            yalign 0
            idle "vivienne full"
            action Jump("part1_meet_viv")