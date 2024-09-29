label part4_start:
    $part = 4
    scene black with fade
    $ renpy.sound.set_volume(0.0,1.0,"ambience")
    $ renpy.sound.set_volume(0.0,1.0,"noise")
    $ renpy.sound.set_volume(0.0,1.0,"sound")
    $ renpy.music.set_volume(1.0,0.0,"music")
    play music "moody progression (halloween ambience).mp3"
    scene bg corpse_plant_night with fade
    $ renpy.sound.set_volume(1.0,0.5,"sound")
    n "Night falls. The stench of the corpse plant is unbearable."
    n "I can't leave. Not now. I have to know."
    n "The smell is making me delirious. I stumble out from behind the tree toward the corpse plant."

    
    play vo "steph ghost voice get out.mp3" noloop
    s "Get out! She sees everything! She knows everything!"
    p "I think I heard something strange…"
    play vo "steph ghost voice escaping her.mp3" noloop
    s "There's no escaping her!"
    play vo "steph ghost voice nooo.mp3" noloop
    s "Noooooo!"
    p "I think I just heard Stephanie. Or maybe the flower's stench is just getting to my head."

    play vo "moreno lazy writing.mp3" noloop
    moreno "Lazy writing? I've got a story that's not lazy!"
    play vo "moreno lets see him.mp3" noloop
    moreno "Let's see him try to write 1,000 words in half an hour!"
    play vo "moreno why cant he.mp3" noloop
    moreno "Why can't he cover this plant story? This lady gives me the creeps!"
    play vo "moreno escaping.mp3" noloop
    moreno "There's no escaping her!"
    p "That sounded like Moreno! I knew he'd never quit without notice!"

    play vo "howard dont trust.mp3" noloop
    howard "I just don't trust you, Honey."
    play vo "howard what to do.mp3" noloop
    howard "I just don't know what to do about her anymore…"
    play vo "howard one eye open.mp3" noloop
    howard "I have to sleep with one eye open or she'll get me…"
    play vo "howard no escape.mp3" noloop
    howard "There's no escaping her!"
    p "The plant is talking! It sounds like Howard was onto Vivienne before she killed him!"

    play vo "nun hail mary.mp3" noloop
    nun "Hail Mary, full of grace…"
    play vo "nun pray for us.mp3" noloop
    nun "Pray for us sinners…"
    play vo "nun now and.mp3" noloop
    nun "Now and at the hour of our death…"
    play vo "nun lord strike.mp3" noloop
    nun "The Lord shall strike down upon thee!"
    p "Of course, the nun is in there. Vivienne won't get away with this!"
    p "I'd better get out before I'm next!"
    p "Uh oh…"
    play vo "viv what are you doing.mp3" noloop
    show vivienne angry_folded
    menu:
        v "You nosy journalist! How dare you be in here without my permission!"
        "I think your plant is talking!":
            call suspicion(-10)
            show vivienne angry_armup
            play vo "voices/Vivienne/viv_1_yoshi_kodachi.mp3" noloop
            menu:
                v "Of course it's talking! It tells me to feed her more, more! Every body brings a new bloom!"
                "That's not what I heard.":
                    call suspicion(25, "death_corpse_plant")
                    v "How dare you! This plant speaks only to me!"
                "Is that where Stephanie went?":
                    call suspicion(-10)
                    show vivienne angry_armup
                    play vo "voices/Vivienne/viv_1_yoshi_mocking.mp3" noloop
                    v "Stephanie was a lousy botanist! Her blood will make my plants grow bigger and better than she ever could!"
        "How many people have you killed here?":
            call suspicion(25, "death_corpse_plant")
            show vivienne angry_armup
            v "That's none of your business! I should have you arrested for trespassing!"
        "You'll never get away with this!":
            play vo "voices/Vivienne/viv_1_yoshi_kodachi.mp3" noloop
            show vivienne angry_armup
            v "Of course I will! I always do! My girl needs to feed!"
            call suspicion(100, "death_bad_end")

    play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop        
    n "Vivienne lunges forward to tackle you, but you duck first."
    p "This one's for Stephanie!"
    $ renpy.sound.set_volume(1.0,0.0,"sound")

    hide vivienne
    hide screen suspicion_bar
    scene bg vivienne_death with fade

    play sound "vivenne death 2.mp3" noloop
    n "Vivienne screams as you toss her into the jaws of the corpse flower."

    n "Her screams fill the greenhouse as she is ripped apart by her precious creation."
    n "The plant licks up every last bit of her flesh with its giant tongue and lets out a loud belch."
    $ renpy.sound.set_volume(1.0,0.0,"noise")
    play noise "burp.mp3" noloop
    $ renpy.music.set_volume(0.0,3.0,"music")
    $ renpy.music.set_volume(1.0,3.0,"ambience")
    play ambience "garden trip hop esque groove with birds.mp3" loop 
    jump credits