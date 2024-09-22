label part2_stephanie_conv:
    $part2_stephanie_conv = True
    menu:
        s "Hello again. Did you enjoy the greenhouse?"
        "No. I found it very disturbing.":
            menu:
                s "I see. You must have plenty of information for your article then."
                "Yes I do.":
                    pass
                "I may have a few more questions...":
                    menu:
                        s "You may want to see the plants at night. That might give you some answers I can’t..."
                        "What answers?":
                            s "I can't say. You should go."
                        "That sounds suspicious.":
                            s "You're right. You should go."
        "I did! The plants are very peaceful.":
            s "I'm so happy to hear that. Please come back later to see the bloom."
        "It's definitely... interesting.":
            menu:
                s "What did you find so interesting?"
                "Your boss":
                    "You should go before she sees me talking with you."
                "The plants.":
                    menu:
                        s "The plants are more interesting at night. They have a way of coming alive."
                        "Vivienne didn't mention that":
                            s "It's one of her secrets. Now leave before it's too late!"
                        "What do you mean by that?":
                            s "Just wait around a bit and you'll see. Now go!"
    # show viv
    v "Stephanie! Stephanie! Where is that lazy girl when you need her?"
    s "What are you still doing here? We don’t appreciate your kind around here!"
    menu:
        s "Don’t try to speak to me again you rude journalist!"
        "Are you OK?":
            "No! Hurry, before she sees you!"
        "Hey! What was that for?":
            "I told you to scram!"
    n "You leave, just before Vivienne finds Stephanie."
    jump part3_start
