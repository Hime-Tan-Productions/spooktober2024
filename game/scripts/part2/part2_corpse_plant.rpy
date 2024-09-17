label part2_corpse_plant:
    scene bg corpse_plant_room with fade
    menu:
        v "Here she is! Isn't she a beauty?"
        "Yes":
            jump part2_viv_scent
        "It's exquisite!":
            call suspicion(-10)
            jump part2_viv_scent
        "It's a little odd, isn't it?":
            call suspicion(10)
            jump part2_viv_odd

label part2_viv_odd:
    menu:
        v "Why would you say such a thing?"
        "I've never seen a flower so large.":
            v "V That’s right! It’s the largest corpse flower known to man. Even larger than those in the wild!"
            p "How does it grow larger than a corpse flower in the jungle?"
            menu:
                v "Do you doubt my abilities as a botanist?"
                "Yes":
                    v "Well, I doubt your abilities as a journalist!"
                    call suspicion(20, death_corpse_flower)
                    jump part2_viv_aroma
                "No":
                    call suspicion(-5)
                    jump part2_viv_aroma

        "The smell is very overpowering. in my life.":
            v "I'll show you something powerful!"
            call suspicion(100, death_corpse_flower)


label part2_viv_scent:
    menu:
        v "Do you smell the scent?"
        "I couldn't miss it!":
            call suspicion(-10)
        "I've never smelled anything so foul in my life.":

            v "I'll show you something foul!"
            call suspicion(10, death_corpse_flower)
    jump part2_viv_aroma


label part2_viv_aroma:
    v "The flower's aroma attracts creatures that feed on carcasses. Flesh flies, dung beetles, sweat bees. They can smell it a half mile away!"
    n "This woman seems oddly happy about death and rotting flesh."
    menu:
        "It smells wonderful!":
            v "I agree! I'd bottle it for perfume if I could!"
            p "What a splendid idea!"
        "Why do you grow this flower if it smells so bad?":
            menu:
                v "Just look at this beauty! It’s a magnificent magenta, don’t you think?"
                "Of course! I've never witnessed such beauty!":
                    call suspicion(-5)
                "I prefer tulips.":
                    call suspicion(10)

        "How can you stand the smell?":
            v "My flower is magnificent. It’s you I can’t stand!"
            call suspicion(10)

    jump part2_viv_infrequent_blooms


label part2_viv_infrequent_blooms:
    menu:
        v "My sweet girl is a rare beauty. Some corpse flowers only bloom once a decade."
        "No wonder everyone wants to see it!":
            call suspicion(-10)            
            v "It's certainly something not to miss!"
            p "I can't wait to see it when it's fully bloomed tonight."
            v "Why don't you view the rest of my greenhouse while we wait?"
            jump part2_corpse_plant_end
        "Is this your first bloom?":
            menu:
                v "No. I have experienced this beauty before."
                "When did the flower last bloom?":
                    menu:
                        v "Why focus on the past? You have the privilege of seeing this marvel in the present!"
                        "Right. I’m grateful for the honor.":
                            call suspicion(-5)
                        "Just trying to get my word count up for the article.":
                            call suspicion(5)
                            v "If word count is what you're after, I can show you the rest of my plants."
        "Maybe it's a good thing.":
            call suspicion(5)
            menu:
                v "Do you believe my work is not important?"
                "I just don't think we need this stinking up the town any more often.":
                    v "I'll rid the town of something it doesn't need!"
                "Wouldn't more frequent blooms diminish its significance?":
                    v "Every bloom she graces us with is significant."
                    v "Perhaps my other plants shall impress you."
                    v "Not that I’m trying to impress you. I already know I have the finest in the land."


    jump part2_corpse_plant_end

label part2_corpse_plant_end:
    menu:
        v "Would you like to see the rest of my greenhouse?"
        "Yes":
            jump part2_banana_tree
        "Maybe later":
            call under_construction
        "No":
            n "Game over"
