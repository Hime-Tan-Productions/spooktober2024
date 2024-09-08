screen mansion_interior_left():
    textbutton "Right":
        xalign 0.75
        yalign 0.5
        action Jump("part1_main")
    imagebutton:
        xalign 0.75
        yalign 0
        idle "stephanie full"
        action Jump("part1_meet_steph")