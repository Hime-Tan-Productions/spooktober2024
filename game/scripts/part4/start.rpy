label part4_start:
    $part = 4
    scene black with fade
    $ renpy.sound.set_volume(0.0,1.0,"ambience")
    $ renpy.sound.set_volume(0.0,1.0,"noise")
    $ renpy.sound.set_volume(0.0,1.0,"sound")
    $ renpy.music.set_volume(1.0,0.0,"music")
    play music "moody progression (halloween ambience).mp3"
    scene bg corpse_plant_night with fade
    $ renpy.sound.set_volume(1.0,0.0,"sound")
    p "Night falls. The stench of the corpse plant is unbearable."
    p "But I can't leave. Not now. I have to know."
    p "The smell is making me delirious. I stumble out from behind the plant toward the corpse plant."

    s "Get out! She sees everything! She knows everything!"
    p "I think I heard something strange…"
    s "There's no escaping her!"
    s "Noooooo!"
    p "I think I just heard Stephanie. Or maybe the flower's stench is just getting to my head."

    moreno "Lazy writing? I've got a story that's not lazy!"
    moreno "Let's see him try to write 1,000 words in half an hour!"
    moreno "Why can't he cover this plant story?"
    moreno "This lady gives me the creeps!"
    moreno "There's no escaping her!"
    p "That sounded like Moreno! I knew he'd never quit without notice!"

    howard "I just don't trust you, Honey."
    howard "I just don't know what to do about her anymore…"
    howard "I have to sleep with one eye open or she'll get me…"
    howard "There's no escaping her!"
    p "The plant is talking! It sounds like Howard was onto Vivienne before she killed him!"


    nun "Hail Mary, full of grace…"
    nun "Pray for us sinners…"
    nun "Now and at the hour of our death…"
    nun "The Lord shall strike down upon thee!"
    p "Of course, the nun is in there. Vivienne won't get away with this!"

    p "I'd better get out before I'm next!"
    p "Uh oh…"
    show vivienne angry_folded
    menu:
        v "You nosy journalist! How dare you be in here without my permission!"
        "I think your plant is talking!":
            call suspicion(-10)
            menu:
                v "Of course it's talking! It tells me to feed her more, more! Every body brings a new bloom!"
                "That's not what I heard.":
                    call suspicion(25)
                    v "How dare you! This plant speaks only to me!"
                "Is that where Stephanie went?":
                    call suspicion(-10)
                    v "Stephanie was a lousy botanist! Her blood will make my plants grow bigger and better than she ever could!"
        "How many people have you killed here?":
            call suspicion(25)
            v "That's none of your business! I should have you arrested for trespassing!"
        "You'll never get away with this!":
            v "Of course I will! I always do! My girl needs to feed!"
            call suspicion(100, "death_bad_end")
    n "Vivienne lunges forward to tackle you, but you duck first."
    p "This one's for Stephanie!"
    $ renpy.sound.set_volume(1.0,0.0,"sound")
    play sound "vivenne death 2.mp3" noloop
    n "Vivienne screams as you toss her into the jaws of the corpse flower."
    n "Her screams fill the greenhouse as she is ripped apart by her precious creation."
    n "The plant licks up every last bit of her flesh with its giant tongue and lets out a loud belch."
    $ renpy.sound.set_volume(1.0,0.0,"noise")
    play noise "burp.mp3" noloop
    jump credits