label part1_meet_viv:
    show screen suspicion_bar
    show vivienne conversation1
    v "Who are you? Oh, that reporter? Fine, I guess I have a few minutes. What do you want to know?"
    jump part1_viv_qs

label part1_viv_qs:
    menu: 
        "Make it quick."
        "Ask a softball question.":
            jump viv_ask_softball
        "Ask about her husband.":
            jump viv_ask_husband
        "Ask about her.":
            jump viv_ask_herself
        "That's all.":
            hide vivienne
            jump part1_main

label viv_ask_softball:
    call suspicion(1)

    p "How many plants does the greenhouse have?"
    v "Far too many to count. But then, it's not the quantity we are known for. It's the quality. Like our renowned Corpse Plant."
    jump part1_viv_qs

label viv_ask_husband:
    p "It must have been terrible, losing your husband."
    show vivienne angry
    call suspicion(50, "death_banana")
    v "I can't stand these types of questions. I've answered them again and again. I had hoped that you were here for more relevant information."
    jump part1_viv_qs

label viv_ask_herself:
    call suspicion(-20)
    p "What is your daily routine like?"
    show vivienne conversation1
    v "I spend most of my time caring for my plants. From dawn till dusk, that's all that's on my mind."
    jump part1_viv_qs