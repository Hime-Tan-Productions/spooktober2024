label part2_start:
    $part = 2
    $ renpy.music.set_volume(0.0,1.0,"music")
    $ renpy.sound.set_volume(0.0,1.0,"nature")
    $ renpy.sound.set_volume(0.0,1.0,"other")
    $ renpy.sound.set_volume(0.0,1.0,"noise")
    $ renpy.sound.set_volume(0.0,1.0,"sound")
    scene black with fade
    play music "corpse flower 3.mp3" loop
    $ renpy.music.set_volume(0.5,0.0,"music")
    play sound "insect sounds 3.mp3" loop
    $ renpy.sound.set_volume(0.8,2.0,"sound")
    jump part2_corpse_plant
