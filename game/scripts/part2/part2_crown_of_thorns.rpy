label part2_viv_crown_of_thorns_interview:
    $int_crown_of_thorns = True

    v "This here is my Crown of Thorns! I bred it to have the sharpest thorns of any plant in the world!"
    menu:
        "How do you know the thorns are the sharpest?":
            v "Would you like to find out?"
            call suspicion(5, "death_crown_of_thorns")
            menu:
                "Yes":
                    call suspicion(100, "death_crown_of_thorns")
                "No":
                    v "I thought so! Enough of your rude questions!"
        "How do you breed your plants?":
            call suspicion(-5)
            menu:
                v "It's all about using the right fertilizer."
                "What type of fertilizer do you use?":
                    v "Why, only the freshest, natural, organic fertilizer for my plants. The fresher, the better!"
                "Where do you get your fertilizer?":
                    call suspicion(5, "death_crown_of_thorns")
                    v "I suppose you’d also like to see the faucet where my water comes from? I’m not asking you where you got your stupid little notebook, now am I?"
    menu:
        v "This plant is quite special. It comes from the personal collection of a dearly departed nun. She left it to me. "
        "Why did she leave it to you?":
            call suspicion(5, "death_crown_of_thorns")
            v "I am a very holy woman!"
        "How do you care for the plant?":
            call suspicion(-5)
            v "It’s a succulent, so I barely have to water it. In fact, I don’t give it any water at all!"

    jump koi_thorns_room