label part2_corpse_plant:
    scene bg corpse_plant with fade
    call screen mansion_interior_corpse_plant


label part2_viv_corpse_plant_interview:
    $int_corpse_flower = True
    show vivienne happy_armup
    play vo "voices/Vivienne/viv_3_yoshi_normal.mp3" noloop
    menu:
        v "Here she is! Isn't she a beauty?"
        "Yes":
            jump part2_viv_scent
        "It's exquisite!":
            call suspicion(-10) from _call_suspicion_13
            jump part2_viv_scent
        "It's a little odd, isn't it?":
            call suspicion(25, "death_corpse_plant") from _call_suspicion_14
            jump part2_viv_odd

label part2_viv_odd:
    show vivienne angry_armup
    play vo "voices/Vivienne/viv_2_yoshi_normal_2.mp3" noloop
    menu:
        v "Why would you say such a thing?"
        "I've never seen a flower so large.":
            show vivienne happy_armup
            play vo "voices/Vivienne/yoshi_short_laugh_4.mp3" noloop
            v "That's right! It's the largest corpse flower known to man. Even larger than those in the wild!"
            show vivienne neutral_folded
            p "How does it grow larger than a corpse flower in the jungle?"
            show vivienne angry_folded
            play vo "voices/Vivienne/viv_2_yoshi_tired.mp3" noloop
            menu:
                v "Do you doubt my abilities as a botanist?"
                "Yes":
                    play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop
                    v "Well, I doubt your abilities as a journalist!"
                    call suspicion(100, "death_corpse_plant") from _call_suspicion_15
                    jump part2_viv_aroma
                "No":
                    call suspicion(-10) from _call_suspicion_16
                    jump part2_viv_aroma

        "The smell is very overpowering.":
            show vivienne angry_folded
            play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop
            v "I'll show you something powerful!"
            $ renpy.music.set_volume(0.0,1.0,"music")
            $ renpy.sound.set_volume(0.0,0.0,"other")
            $ renpy.sound.set_volume(0.0,0.0,"noise")
            $ renpy.sound.set_volume(0.0,0.0,"sound")
            play death "it was you (harsh horror reveal strings).mp3" loop
            $ renpy.sound.set_volume(1.0,0.0,"death")
            call suspicion(100, "death_corpse_plant") from _call_suspicion_17


label part2_viv_scent:
    show vivienne neutral_armup_mouthopen
    menu:
        v "Do you smell the scent?"
        "I couldn't miss it!":
            call suspicion(-10) from _call_suspicion_18
        "I've never smelled anything so foul in my life.":
            show vivienne angry_folded
            play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop
            v "I'll show you something foul!"
            $ renpy.music.set_volume(0.0,1.0,"music")
            $ renpy.sound.set_volume(0.0,0.0,"other")
            $ renpy.sound.set_volume(0.0,0.0,"noise")
            $ renpy.sound.set_volume(0.0,0.0,"sound")
            play death "it was you (harsh horror reveal strings).mp3" loop
            $ renpy.sound.set_volume(1.0,0.0,"death")
            call suspicion(100, "death_corpse_plant") from _call_suspicion_19
    jump part2_viv_aroma


label part2_viv_aroma:
    show vivienne happy_folded
    play vo "voices/Vivienne/yoshi_short_laugh.mp3" noloop
    v "The flower's aroma attracts creatures that feed on carcasses. Flesh flies, dung beetles, sweat bees. They can smell it a half mile away!"
    n "This woman seems oddly happy about death and rotting flesh."
    show vivienne neutral_folded
    menu:
        "It smells wonderful!":
            call suspicion(-10) from _call_suspicion_20
            show vivienne happy_folded
            play vo "voices/Vivienne/yoshi_short_laugh_2.mp3" noloop
            v "I agree! I'd bottle it for perfume if I could!"
            p "What a splendid idea!"
        "Why do you grow this flower if it smells so bad?":
            play vo "voices/Vivienne/viv_2_yoshi_normal_2.mp3" noloop
            show vivienne angry_folded
            menu:
                v "Just look at this beauty! It's magnificent, don't you think?"
                "Of course! I've never witnessed such beauty!":
                    call suspicion(-10) from _call_suspicion_21
                    play vo "voices/Vivienne/yoshi_short_laugh_4.mp3" noloop
                "I prefer tulips.":
                    show vivienne angry_folded
                    call suspicion(25, "death_corpse_plant") from _call_suspicion_22

        "How can you stand the smell?":
            play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop
            show vivienne angry_folded
            v "My flower is magnificent. It's you I can't stand!"
            call suspicion(100, "death_corpse_plant") from _call_suspicion_23

    jump part2_viv_infrequent_blooms


label part2_viv_infrequent_blooms:
    show vivienne neutral_armup_mouthopen
    menu:
        v "My sweet girl is a rare beauty. Some corpse flowers only bloom once a decade."
        "No wonder everyone wants to see it!":
            call suspicion(-10) from _call_suspicion_24            
            show vivienne happy_folded
            v "It's certainly something not to miss!"
            p "I can't wait to see it when it's fully bloomed tonight."
            jump part2_corpse_plant_end
        "Is this your first bloom?":
            show vivienne neutral_folded_mouthopen
            menu:
                v "No. I have experienced this beauty before."
                "When did the flower last bloom?":
                    call suspicion(25, "death_corpse_plant") from _call_suspicion_25
                    play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop
                    show vivienne angry_folded
                    menu:
                        v "Why focus on the past? You have the privilege of seeing this marvel in the present!"
                        "Right. I'm grateful for the honor.":
                            show vivienne happy_folded
                            play vo "voices/Vivienne/viv_1_yoshi_mocking.mp3" noloop
                            call suspicion(-10) from _call_suspicion_26
                            v "In that case, I'd love to show you more!"
                            jump corpse_plant_room
                        "Just trying to get my word count up for the article.":
                            call suspicion(25, "death_corpse_plant") from _call_suspicion_27
                            v "If word count is what you're after, I can show you the rest of my greenhouse."
                "How many times has this flower bloomed?":
                    menu:
                        v "This is her third bloom."
                        "This one must be extra special! The third time is the charm.":
                            call suspicion(-10) from _call_suspicion_28
                        "How have you been so lucky?":
                            call suspicion(25, "death_corpse_plant") from _call_suspicion_29
                            show vivienne happy_armup
                            play vo "voices/Vivienne/viv_1_yoshi_kodachi.mp3" noloop
                            menu:
                                v "Isn't it obvious? I'm the finest botanist in the U.S. Probably the world!"
                                "Of course you are.":
                                    call suspicion(-10) from _call_suspicion_30
                                "If you say so.":
                                    call suspicion(25, "death_corpse_plant") from _call_suspicion_31
        "Maybe it's a good thing.":
            show vivienne angry_armup
            call suspicion(25, "death_corpse_plant") from _call_suspicion_32
            play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop
            menu:
                v "Do you believe my work is not important?"
                "I just don't think we need this stinking up the town any more often.":
                    v "I'll rid the town of something it doesn't need!"
                    call suspicion(100, "death_corpse_plant") from _call_suspicion_33
                "Wouldn't more frequent blooms diminish its significance?":
                    show vivienne neutral_folded
                    play vo "voices/Vivienne/viv_2_yoshi_normal_2.mp3" noloop
                    v "Every bloom she graces us with is significant."
                    jump part2_corpse_plant_end

    jump part2_corpse_plant_end

label part2_corpse_plant_end:
    show vivienne neutral_folded_mouthopen
    v "Perhaps my other plants shall impress you."
    play vo "voices/Vivienne/yoshi_short_laugh_3.mp3" noloop
    show vivienne happy_folded
    v "Not that I'm trying to impress you. I already know I have the finest in the land."
    jump corpse_plant_room