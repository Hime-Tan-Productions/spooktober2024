label part2_sister_garcia:
    call suspicion(10, "death_crown_of_thorns")
    menu:
        p "What should I ask Vivienne?"
        "How do you know Sister Garcia?":
            show vivienne angry_armup
            play vo "voices/Vivienne/viv_2_yoshi_normal_2.mp3" noloop
            v "Why, I'm the biggest donor to the church in town! Everyone knows my name."
            jump koi_thorns_room
        "Tell me about how you got her plant again.":
            call suspicion(25, "death_crown_of_thorns")
            show vivienne angry_armup
            play vo "voices/Vivienne/viv_2_yoshi_tired.mp3" noloop
            menu:
                v "Don't be dim! After she died I replanted it from her personal collection."
                "I remember her name from the cold case files.":
                    call suspicion(-10)
                    show vivienne angry_folded
                    play vo "voices/Vivienne/viv_2_yoshi_normal_2.mp3" noloop
                    menu:
                        v "Do you now? You're not as stupid as I thought then!"
                        "I may be stupid. But at least I know a cold case means the person was never declared dead.":
                            call suspicion(100, "death_crown_of_thorns")
                        "I may be smarter than you.":
                            call suspicion(-10)
                            show vivienne happy_armup
                            play vo "voices/Vivienne/viv_1_yoshi_mocking.mp3" noloop
                            v "Haha! Don't make me laugh. Actually, laughter is good for plants. Can't you tell?"
                            jump koi_thorns_room
                "I reported on her disappearance when she never returned to the church.":
                    call suspicion(25, "death_crown_of_thorns")
                    show vivienne angry_armup
                    play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop 
                    v "I don't want to talk any more about that nun! Can't you see I'm mourning her death?"
                    jump koi_thorns_room
