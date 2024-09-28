screen mansion_interior_banana():
    $right = False

    if part == 1 or part == 2:
        $right = True

    if right:
        imagebutton:
            xalign 0.9
            yalign 0.5
            idle "right"
            action [Stop("sound", fadeout=1.0),Pause(1.0),Stop("other"),Stop("noise"),Play("ambience","koi pond water noises.mp3"),Play("other","heater sounds 5.mp3"),Play("noise","sprinkler system 2.mp3"),Function(renpy.sound.set_volume, 0.5, channel="ambience"),Function(renpy.sound.set_volume, 0.25, channel="other"),
        Function(renpy.sound.set_volume, 0.4, channel="noise"),Jump("koi_thorns_room")]

            


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
