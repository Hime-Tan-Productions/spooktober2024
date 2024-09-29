label banana_room:
    scene bg banana_room
    $ renpy.sound.set_volume(0.0,0.8,"nature")
    $ renpy.sound.set_volume(0.0,0.8,"other")
    $ renpy.sound.set_volume(0.0,0.8,"noise")
    play noise "sprinkler system 2.mp3" loop
    $ renpy.sound.set_volume(0.6,0.0,"noise")
    play sound "tropic birds.mp3" loop
    $ renpy.sound.set_volume(0.075,0.0,"sound")
    if part == 1:
        if not met_stephanie:
            p "At least the plants are nice here. The people… not so much."
            p "Why do I always feel like trees are trying to tell me something?"
            play other "in the grass.mp3"
            $ renpy.sound.set_volume(0.4,0.5,"other")
            p "Is something moving in the plants?"
            p "It's… a person?"
            show stephanie full_day
            pause
            jump part1_meet_steph
    elif part == 2:
        if not int_banana_tree:
            menu:
                n "I'm in the banana tree room."
                "Ask Vivienne for an interview about the banana tree.":
                    n "I track down Vivienne."
                    jump part2_viv_banana_tree_interview
                "Look around":
                    pass

    elif part == 3:
        jump banana_hide_choices
    call screen mansion_interior_banana

label banana_hide_choices:
    menu: 
        n "Where should I hide?"
        "Behind the banana tree.":
            p "That's right! Stephanie said she would hide from Vivienne there!"
            p "Now to wait for night."
            jump part4_start
        "Somewhere else.":
            jump banana_room

