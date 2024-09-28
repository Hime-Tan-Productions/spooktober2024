label part2_corpse_plant:
    scene bg corpse_plant with fade
    call screen mansion_interior_corpse_plant


label part2_viv_corpse_plant_interview:
    $int_corpse_flower = True
    menu:
        v "Here she is! Isn't she a beauty?"
        "Yes":
            jump part2_viv_scent
        "It's exquisite!":
            call suspicion(-10)
            jump part2_viv_scent
        "It's a little odd, isn't it?":
            call suspicion(25, "death_corpse_plant")
            jump part2_viv_odd

label part2_viv_odd:
    menu:
        v "Why would you say such a thing?"
        "I've never seen a flower so large.":
            v "That's right! It's the largest corpse flower known to man. Even larger than those in the wild!"
            p "How does it grow larger than a corpse flower in the jungle?"
            menu:
                v "Do you doubt my abilities as a botanist?"
                "Yes":
                    v "Well, I doubt your abilities as a journalist!"
                    call suspicion(100, "death_corpse_plant")
                    jump part2_viv_aroma
                "No":
                    call suspicion(-10)
                    jump part2_viv_aroma

        "The smell is very overpowering.":
            v "I'll show you something powerful!"
            $ renpy.music.set_volume(0.0,1.0,"music")
            $ renpy.sound.set_volume(0.0,0.0,"other")
            $ renpy.sound.set_volume(0.0,0.0,"noise")
            $ renpy.sound.set_volume(0.0,0.0,"sound")
            play death "it was you (harsh horror reveal strings).mp3" loop
            $ renpy.sound.set_volume(1.0,0.0,"death")
            call suspicion(100, "death_corpse_plant")


label part2_viv_scent:
    menu:
        v "Do you smell the scent?"
        "I couldn't miss it!":
            call suspicion(-10)
        "I've never smelled anything so foul in my life.":

            v "I'll show you something foul!"
            $ renpy.music.set_volume(0.0,1.0,"music")
            $ renpy.sound.set_volume(0.0,0.0,"other")
            $ renpy.sound.set_volume(0.0,0.0,"noise")
            $ renpy.sound.set_volume(0.0,0.0,"sound")
            play death "it was you (harsh horror reveal strings).mp3" loop
            $ renpy.sound.set_volume(1.0,0.0,"death")
            call suspicion(100, "death_corpse_plant")
    jump part2_viv_aroma


label part2_viv_aroma:
    v "The flower's aroma attracts creatures that feed on carcasses. Flesh flies, dung beetles, sweat bees. They can smell it a half mile away!"
    n "This woman seems oddly happy about death and rotting flesh."
    menu:
        "It smells wonderful!":
            call suspicion(-10)
            v "I agree! I'd bottle it for perfume if I could!"
            p "What a splendid idea!"
        "Why do you grow this flower if it smells so bad?":
            menu:
                v "Just look at this beauty! It's magnificent, don't you think?"
                "Of course! I've never witnessed such beauty!":
                    call suspicion(-10)
                "I prefer tulips.":
                    call suspicion(25, "death_corpse_plant")

        "How can you stand the smell?":
            v "My flower is magnificent. It's you I can't stand!"
            call suspicion(100, "death_corpse_plant")

    jump part2_viv_infrequent_blooms


label part2_viv_infrequent_blooms:
    menu:
        v "My sweet girl is a rare beauty. Some corpse flowers only bloom once a decade."
        "No wonder everyone wants to see it!":
            call suspicion(-10)            
            v "It's certainly something not to miss!"
            p "I can't wait to see it when it's fully bloomed tonight."
            jump part2_corpse_plant_end
        "Is this your first bloom?":
            menu:
                v "No. I have experienced this beauty before."
                "When did the flower last bloom?":
                    call suspicion(25, "death_corpse_plant")
                    menu:
                        v "Why focus on the past? You have the privilege of seeing this marvel in the present!"
                        "Right. I'm grateful for the honor.":
                            call suspicion(-10)
                            v "In that case, I'd love to show you the rest of my plants!"
                        "Just trying to get my word count up for the article.":
                            call suspicion(25, "death_corpse_plant")
                            v "If word count is what you're after, I can show you the rest of my plants."
                "How many times has this flower bloomed?":
                    menu:
                        v "This is her third bloom."
                        "This one must be extra special! The third time is the charm.":
                            call suspicion(-10)
                        "How have you been so lucky?":
                            call suspicion(25, "death_corpse_plant")
                            menu:
                                v "Isn't it obvious? I'm the finest botanist in the U.S. Probably the world!"
                                "Of course you are.":
                                    call suspicion(-10)
                                "If you say so.":
                                    call suspicion(25, "death_corpse_plant")
        "Maybe it's a good thing.":
            call suspicion(25, "death_corpse_plant")
            menu:
                v "Do you believe my work is not important?"
                "I just don't think we need this stinking up the town any more often.":
                    v "I'll rid the town of something it doesn't need!"
                    call suspicion(100, "death_corpse_plant")
                "Wouldn't more frequent blooms diminish its significance?":
                    v "Every bloom she graces us with is significant."
                    v "Perhaps my other plants shall impress you."
                    v "Not that I'm trying to impress you. I already know I have the finest in the land."

    jump part2_corpse_plant_end

label part2_corpse_plant_end:
    v "Perhaps my other plants shall impress you."
    v "Not that I'm trying to impress you. I already know I have the finest in the land."
    jump corpse_plant_room