label part3_start:
    scene black with fade
    $ renpy.sound.set_volume(0.0,1.0,"sound")
    $ renpy.sound.set_volume(0.0,1.0,"noise")
    $ renpy.sound.set_volume(0.0,1.0,"ambience")
    $ renpy.sound.set_volume(0.0,1.0,"other")
    $ renpy.sound.set_volume(0.0,1.0,"nature")
    play music "creepy wind chime melody.mp3"
    n "<part 3 intro. It's time for the showing.>"
    $part = 3
    scene bg corpse_plant_crowd with fade
    $ renpy.sound.set_volume(0.6,1.0,"sound")
    play sound "insect sounds 3.mp3" loop
    $ renpy.sound.set_volume(0.6,1.0,"noise")
    play noise "crowd 2.mp3" loop
    p "Half the county appears to have come to see the corpse plant open to its fully glory."
    $ renpy.sound.set_volume(0.9,1.0,"nature")
    play nature "flies 2.mp3" noloop
    p "With its petals fully bloomed, the air smells even more strongly of rotting meat, soiled laundry, and moldy cheese left in a garbage can to cook in the hot sun all day."
    p "I'd be emptying my stomach in the ferns if I hadn't already done that after my first visit to the greenhouse."

    show vivienne
    $ renpy.sound.set_volume(0.0,2.0,"nature")
    v "Ladies and gentleman, I present to you the eighth wonder of the world!"
    $ renpy.sound.set_volume(0.8,0.0,"other")
    play other "applause 2.mp3" noloop
    n "Sound of applause"
    v "Here you see that my girl has done it again. Her third bloom this year! I see many more in her future."
    v "Take as many photos as you wish! Make sure you get both our good sides!"
    n "<wait for player to click on Stephanie's glasses>"
    $ renpy.sound.set_volume(0.0,2.0,"music")
    $ renpy.sound.set_volume(0.6,0.5,"ambience")
    play ambience "corpse flower mystic mix.mp3"
    p "Where's Stephanie? Something tells me this can't be good..."
    v "No time for questions! Everyone out by sundown. My girls needs her beauty sleep."
    menu:
        p "What should I do?"
        "I have enough for my story. Time to move on.":
            call suspicion(100, "ending_walk_away")
        "I want to know more.":
            p "Something is wrong."
    menu:
        p "I need to know..."
        "What happened to Moreno?":
            pass
        "Where is Stephanie?":
            pass
        "What about Sister Garcia?":
            pass
        "How did her husband die?":
            pass

    p "I have a bad feeling that I know the answer."
    menu:
        p "Stephanie mentioned that strange things happen at night."
        "I should hide and wait for night.":
            p "I find a little nook that has "
            pass
        "I should confront Vivienne.":
            call suspicion(100, "death_vivienne_confrontation")
            pass
        "I should call the police.":
            call suspicion(100, "death_vivienne_call_police")
            pass
    jump part4_start