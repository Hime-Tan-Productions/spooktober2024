label part4_start:
    $part = 4
    scene bg corpse_plant_night with fade
    p "Night falls. The stench of the corpse plant is unbearable."
    p "But I can't leave. Not now. I have to know."
    p "The smell is making me delirious. I stumble out from behind the plant toward the corpse plant."
    "Get out! She sees everything! She knows everything!"
    p "I think I heard something strange..."
    "I just don't trust you, Honey."
    p "What was that?!"
    "Hail Mary, full of grace..."
    p "Is the stench getting to my brain? Or is this plant really talking to me?"
    "There's no escaping her!"
    p "Stephanie?"
    "Noooooo!"
    "Lazy writing? I've got a story that's not lazy!"
    p "Moreno?"
    "I just don't know what to do about her anymore..."
    "Pray for us sinners…"
    p "Sounds like the nun is in here too..."
    "Let’s see him try to write 1,000 words in half an hour!"
    "I have to sleep with one eye open or she’ll get me…"
    "Now and at the hour of our death…"
    "Why can’t he cover this plant story? This lady gives me the creeps!"
    "There’s no escaping her!"
    "The Lord shall strike down upon thee!"
    "There's no escaping her!"
    p "There are definitely voices coming from the plant."
    p "They seem to be coming from the people who disappeared here…"
    p "That Vivienne killed here..."
    p "I'd better get out before I'm next!"
    p "Uh oh..."
    show vivienne
    menu:
        v "You nosy journalist! How dare you be in here without my permission!"
        "I think your plant is talking!":
            call suspicion(-5)
            menu:
                v "Of course it's talking! It tells me to feed her more, more! Every body brings a new bloom!"
                "That's not what I heard.":
                    call suspicion(5)
                    v "How dare you! This plant speaks only to me!"
                "Is that where Stephanie went?":
                    call suspicion(-5)
                    v "Stephanie was a lousy botanist! Her blood will make my plants grow bigger and better than she ever could!Stephanie was a lousy botanist! Her blood will make my plants grow bigger and better than she ever could!"
        "How many people have you killed here?":
            call suspicion(10)
            v "That's none of your business! I should have you arrested for trespassing!"
        "You'll never get away with this!":
            v "Of course I will! I always do! My girl needs to feed!"
            call suspicion(100, "death_bad_end")
    n "Vivienne lunges forward to tackle you, but you duck first."
    p "This one's for Stephanie!"
    n "Vivienne screams as you toss her into the jaws of the corpse flower."
    n "Her screams fill the greenhouse as she is ripped apart by her precious creation."
    n "The plant licks up every last bit of her flesh with its giant tongue and lets out a loud belch."
    jump credits