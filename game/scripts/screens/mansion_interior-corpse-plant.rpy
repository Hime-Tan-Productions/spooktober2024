screen mansion_interior_corpse_plant():
    $left = False

    if part == 2:
        if int_corpse_flower:
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
            action [Stop("sound", fadeout=1.0),Pause(1.0),Stop("other"),Stop("noise"),Play("ambience","koi pond water noises.mp3"),Play("other","heater sounds 5.mp3"),Play("noise","sprinkler system 2.mp3"),Function(renpy.sound.set_volume, 0.5, channel="ambience"),Function(renpy.sound.set_volume, 0.25, channel="other"),
        Function(renpy.sound.set_volume, 0.4, channel="noise"),Jump("part1_main")]