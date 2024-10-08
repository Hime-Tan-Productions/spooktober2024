label part3_start:

    scene black with fade

    $ renpy.sound.set_volume(0.0,1.0,"sound")
    $ renpy.sound.set_volume(0.0,1.0,"noise")
    $ renpy.sound.set_volume(0.0,1.0,"ambience")
    $ renpy.sound.set_volume(0.0,1.0,"other")
    $ renpy.sound.set_volume(0.0,1.0,"nature")
    play music "creepy wind chime melody.mp3"

    $part = 3

    scene bg corpse_plant_crowd with fade
    $ renpy.sound.set_volume(0.6,1.0,"sound")
    play sound "insect sounds 3.mp3" loop
    $ renpy.sound.set_volume(0.6,1.0,"noise")
    play noise "crowd 2.mp3" loop

    p "Half the county appears to have come to see the corpse plant open to its full glory."

    $ renpy.sound.set_volume(0.9,1.0,"nature")
    play nature "flies 2.mp3" noloop

    p "With its petals fully bloomed, the air smells even more strongly of rotting meat, soiled laundry, and moldy cheese left in a garbage can to cook on a hot summer day."
    p "I'd be emptying my stomach in the ferns if I hadn't already."
    
    $ renpy.sound.set_volume(0.0,2.0,"nature")
    
    play vo "voices/Vivienne/viv_my_beautiful_flower_2.mp3" noloop
    show vivienne happy_folded
    v "Ladies and gentlemen, I present to you the eighth wonder of the world!"
    
    $ renpy.sound.set_volume(0.8,0.0,"other")
    play other "applause 2.mp3" noloop
    v "Here you see that my girl has done it again. Her third bloom this year! I see many more in her future."
    show vivienne happy_armup
    v "Take as many photos as you wish! Make sure you get both our good sides!"
    
    hide vivienne

    $ renpy.sound.set_volume(0.0,4.0,"music")
    $ renpy.sound.set_volume(0.6,0.5,"ambience")
    play ambience "corpse flower mystic mix.mp3"
    
    p "Where's Stephanie? Something tells me this can't be good…"
    p "Wait… are those her glasses, by the corpse plant?!"
    $clue_stephanie = True
    show vivienne angry_armup
    v "No time for questions! Everyone out by sundown. My girl needs her beauty sleep."
    hide vivienne
    menu:
        p "What should I do?"
        "I have enough for my story. Time to move on.":
            n "I didn't find anything that makes it worth staying to investigate more."
            n "It's going to be hard to write a good story with so little information."
            n "Oh well, I'm going to just move on."
            jump ending_walk_away
        "I want to know more.":
            p "Something is wrong."
            $chosen = []
            jump ask_clues

label ask_clues:
    menu:
        set chosen
        p "I need to know…"
        "Did Moreno really quit?" if clue_moreno:
            p "I think he may have died while trying to cover this story."
            jump ask_clues
        "Where is Stephanie?" if clue_stephanie:
            p "I have a bad feeling I already know the answer."
            jump ask_clues
        "What happened to Sister Garcia?" if clue_nun:
            p "It seems as if Vivienne may have killed the poor nun to steal her plant."
            jump ask_clues
        "How did Howard die?" if clue_howard:
            p "I'm sure he was poisoned at Vivienne's hands."
            jump ask_clues
    p "Stephanie mentioned that strange things happen at night."

    if not clue_moreno or not clue_stephanie or not clue_nun or not clue_howard:
        p "I can't help feeling like I've missed something."
        jump ending_walk_away
    else:
        menu:
            "I should hide and wait for night.":
                jump ask_hide
            "I should confront Vivienne.":
                call suspicion(100, "death_vivienne_confrontation") from _call_suspicion_53
            "I should call the police.":
                call suspicion(100, "death_vivienne_call_police") from _call_suspicion_54

label ask_hide:
    $ renpy.sound.set_volume(0.9,0.5,"music")
    $ renpy.sound.set_volume(0.0,0.5,"ambience")
    play music "moody progression (we have to hurry intensity).mp3" loop
    p "I need to find a spot where nobody will find me."
    jump corpse_plant_room
