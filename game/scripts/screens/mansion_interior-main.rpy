screen mansion_interior_main():
    textbutton "Left":
        xalign 0.25
        yalign 0.5
        action Jump("part1_left")
    textbutton "Right":
        xalign 0.75
        yalign 0.5
        action Jump("part1_right")
    if "explored_left" in flags.keys() and "explored_right" in flags.keys():
        imagebutton:
            xalign 0.75
            yalign 0
            idle "vivienne full"
            action Jump("part1_meet_viv")