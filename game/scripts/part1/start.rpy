label part1_start:
    $part = 1
    scene bg koi_thorns
    $ renpy.sound.set_volume(0.0,0.1,"nature")
    stop sound
    $ renpy.sound.set_volume(0.55,0.0,"ambience")
    play ambience "door 1.mp3" noloop
    $ renpy.sound.set_volume(0.5,0.0,"nature")
    play nature "koi pond water noises.mp3" loop
    $ renpy.sound.set_volume(0.3,60.0,"nature")
    play other "heater sounds 5.mp3" loop
    $ renpy.sound.set_volume(0.25,0.0,"other")
    play noise "sprinkler system 2.mp3" loop
    $ renpy.sound.set_volume(0.4,0.0,"noise")
    n "The greenhouse welcomes you with a strong scent of vanilla, plus a hint of something rotten. Must be the corpse flower…"
    call screen mansion_interior_koi_thorn

label part1_main:
    jump koi_thorns_room
