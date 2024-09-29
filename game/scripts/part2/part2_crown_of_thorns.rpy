label part2_viv_crown_of_thorns_interview:
    $int_crown_of_thorns = True
    show vivienne neutral_armup_mouthopen
    v "This here is my Crown of Thorns! I bred it to have the sharpest thorns of any plant in the world!"
    menu:
        "How do you know the thorns are the sharpest?":
            call suspicion(25, "death_crown_of_thorns")
            show vivienne happy_armup
            play vo "voices/Vivienne/viv_1_yoshi_triumph.mp3" noloop 
            menu:
                v "Would you like to find out?"
                "Yes":
                    call suspicion(100, "death_crown_of_thorns")
                "No":
                    show vivienne neutral_folded_mouthopen
                    play vo "voices/Vivienne/viv_2_yoshi_normal_2.mp3" noloop
                    v "I thought so! Enough of your rude questions!"
                    show vivienne neutral_armup_mouthopen
        "How do you breed your plants?":
            call suspicion(-10)
            show vivienne neutral_folded_mouthopen
            menu:
                v "It's all about using the right fertilizer."
                "What type of fertilizer do you use?":
                    show vivienne happy_armup
                    play vo "voices/Vivienne/yoshi_short_laugh.mp3" noloop
                    v "Why, only the freshest, natural, organic fertilizer for my plants. The fresher, the better!"
                    show vivienne neutral_armup_mouthopen
                "Where do you get your fertilizer?":
                    call suspicion(25, "death_crown_of_thorns")
                    show vivienne angry_folded
                    play vo "voices/Vivienne/viv_2_yoshi_tired.mp3" noloop
                    v "I suppose you'd also like to see the faucet where my water comes from? I'm not asking you where you got your stupid little notebook, now am I?"
    menu:
        v "This plant is quite special. It comes from the personal collection of a dearly departed nun. She left it to me. "
        "Why did she leave it to you?":
            call suspicion(25, "death_crown_of_thorns")
            show vivienne angry_folded
            play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop
            v "I am a very holy woman!"
        "How do you care for the plant?":
            call suspicion(-10)
            show vivienne neutral_folded
            v "It's a succulent, so I barely have to water it. In fact, I don't give it any water at all!"

    jump koi_thorns_room