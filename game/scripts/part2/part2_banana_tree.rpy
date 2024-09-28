label part2_banana_tree:
    scene bg banana_tree with fade
    call screen mansion_interior_banana

label part2_viv_banana_tree_interview:
    show vivienne happy_armup
    $int_banana_tree = True
    v "I see you found my banana tree!"
    menu:
        v "My husband Howard grew it from a single seed."
        "That's impressive!":
            call suspicion(25, "death_banana")
            v "Not at all! It's a cowardly way to get a new plant."
            menu:
                n "What is this woman's deal? I can't wait to get out of here!"
                "What is the best way to get a new plant?":
                    call suspicion(25, "death_banana")
                    v "You use nature to your advantage, of course. It's how I have the biggest and brightest blooms around."
                    n "These aren't the gardening tips I was hoping for."
                    n "Maybe I should learn more about Howard."
                "What is cowardly about seeds?":
                    call suspicion(-10)
                    v "Seeds are for the weak. I'm willing to go the extra mile for my plants."
                    menu:
                        v "Howard never had the guts like me!"
                        "How do you grow your plants then?":
                            call suspicion(25, "death_banana")
                            v "Ask me about my trade secrets one more time and you'll regret it."
                        "Why didn't Howard have the guts?":
                            call suspicion(-10)
                            v "My Howard never saw eye-to-eye with me! I don't have to worry about that now though."
        "I'm sure you're still a better botanist.":
            call suspicion(-10)
            menu:
                v "I am! Howard never agreed with me on the best gardening methods."
                "What did you disagree on?":
                    v "Howard was never as… innovative as I am."
                    call suspicion(-10)
                "What are the best gardening methods?":
                    v "How dare you ask for my trade secrets!"
                    call suspicion(25, "death_banana")
                    n "It's clear this woman has secrets of some sort. I doubt they all relate to plant care."
    jump part2_bt_howard

label part2_bt_howard:
    menu:
        v "What else would you like to know about my Howard's banana tree?"
        "What happened to Howard?":
            v "Perhaps you'd like to see it as Howard saw it…"
            call suspicion(100, "death_banana")
        "What is your favorite thing about Howard's banana tree?":
            v "I've added my own special touch to the tree… it gives the bananas a little extra flavor."
    jump banana_room