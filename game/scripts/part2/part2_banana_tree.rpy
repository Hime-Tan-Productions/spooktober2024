label part2_banana_tree:
    scene bg banana_tree with fade
    call screen mansion_interior_banana

label part2_viv_banana_tree_interview:
    show vivienne happy_folded
    $int_banana_tree = True
    play vo "voices/Vivienne/yoshi_short_laugh.mp3" noloop
    v "I see you found my banana tree!"
    menu:
        v "My husband Howard grew it from a single seed."
        "That's impressive!":
            call suspicion(25, "death_banana") from _call_suspicion_4
            show vivienne angry_folded
            v "Not at all! It's a cowardly way to get a new plant."
            menu:
                n "What is this woman's deal? I can't wait to get out of here!"
                "What is the best way to get a new plant?":
                    call suspicion(25, "death_banana") from _call_suspicion_5
                    show vivienne happy_armup
                    play vo "voices/Vivienne/viv_1_yoshi_triumph.mp3" noloop 
                    v "You use nature to your advantage, of course. It's how I have the biggest and brightest blooms around."
                    n "These aren't the gardening tips I was hoping for."
                    show vivienne neutral_folded
                    n "Maybe I should learn more about Howard."
                "What is cowardly about seeds?":
                    show vivienne angry_folded
                    call suspicion(-10) from _call_suspicion_6
                    v "Seeds are for the weak. I'm willing to go the extra mile for my plants."
                    menu:
                        v "Howard never had the guts like me!"
                        "How do you grow your plants then?":
                            call suspicion(25, "death_banana") from _call_suspicion_7
                            show vivienne angry_armup
                            play vo "voices/Vivienne/viv_2_yoshi_tired.mp3" noloop
                            v "Ask me about my trade secrets one more time and you'll regret it."
                        "Why didn't Howard have the guts?":
                            call suspicion(-10) from _call_suspicion_8
                            show vivienne neutral_folded_mouthopen
                            v "My Howard never saw eye-to-eye with me! I don't have to worry about that now though."
        "I'm sure you're still a better botanist.":
            show vivienne happy_armup
            call suspicion(-10) from _call_suspicion_9
            play vo "voices/Vivienne/yoshi_short_laugh_3.mp3" noloop
            menu:
                v "I am! Howard never agreed with me on the best gardening methods."
                "What did you disagree on?":
                    show vivienne angry_folded
                    play vo "voices/Vivienne/viv_2_yoshi_tired.mp3" noloop
                    v "Howard was never as… innovative as I am."
                    show vivienne neutral_folded_mouthopen
                    call suspicion(-10) from _call_suspicion_10
                "What are the best gardening methods?":
                    play vo "voices/Vivienne/viv_2_yoshi_normal_2.mp3" noloop
                    show vivienne angry_folded
                    v "How dare you ask for my trade secrets!"
                    call suspicion(25, "death_banana") from _call_suspicion_11
                    n "It's clear this woman has secrets of some sort. I doubt they all relate to plant care."
    jump part2_bt_howard

label part2_bt_howard:
    menu:
        v "What else would you like to know about my Howard's banana tree?"
        "What happened to Howard?":
            show vivienne angry_folded
            play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop
            v "Perhaps you'd like to see it as Howard saw it…"
            call suspicion(100, "death_banana") from _call_suspicion_12
        "What is your favorite thing about Howard's banana tree?":
            show vivienne happy_armup
            play vo "voices/Vivienne/viv_1_yoshi_mocking.mp3" noloop
            v "I've added my own special touch to the tree… it gives the bananas a little extra flavor."
    jump banana_room