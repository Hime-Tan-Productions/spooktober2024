label part2_stephanie_conv:
    $part2_stephanie_conv = True
    show stephanie neutral_lookingup_handsup
    play vo "voices/Stephanie/steph-HowCanIHelp-002.mp3" noloop
    menu:
        s "Hello again. Have you been enjoying the greenhouse?"
        "No. I found it very disturbing.":
            show stephanie neutral_lookingdown_handsup
            menu:
                s "I see. You must have plenty of information for your article then."
                "Yes I do.":
                    s "Don't forget to include that some strange things happen here at night."
                "I may have a few more questions…":
                    show stephanie neutral_lookingup_handsup
                    menu:
                        s "You may want to see the plants at night. That might give you some answers I can't…"
                        "What answers?":
                            s "I can't say. You should go."
                        "That sounds suspicious.":
                            s "You're right. You should go."
        "I did! The plants are very peaceful.":
            show stephanie neutral_lookingdown_handsup
            s "I'm so happy to hear that. Please come back later to see the bloom."
            show stephanie neutral_lookingup_handsup
            s "You may notice some things happening at night that I can't explain."
        "It's definitely… interesting.":
            menu:
                s "What did you find so interesting?"
                "Your boss.":
                    show stephanie neutral_lookingdown_handsup
                    s "You should go before she sees me talking to you."
                    show stephanie neutral_lookingup_handsup
                    s "She may be the cause of some strange things that happen at night!"
                "The plants.":
                    show stephanie neutral_lookingdown
                    menu:
                        s "The plants are more interesting at night. They have a way of coming alive."
                        "Vivienne didn't mention that":
                            show stephanie neutral_lookingup_handsup
                            s "It's one of her secrets. Now leave before it's too late!"
                        "What do you mean by that?":
                            show stephanie neutral_lookingup_handsup
                            s "Just wait around a bit and you'll see. Now go!"
    # show viv?
    show stephanie scared_handsup
    play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop
    v "Stephanie! Stephanie! Where is that lazy girl when you need her?"
    s "What are you still doing here? Get out! We have so much work to do!"
    menu:
        s "Don't try to speak to me again you rude journalist!"
        "Are you OK?":
            play vo "voices/Stephanie/steph-Groan-004.mp3" noloop
            show stephanie scared
            s "No! Hurry, before she sees you!"
        "Hey! What was that for?":
            show stephanie scared
            play vo "voices/Stephanie/steph-Groan-004.mp3" noloop
            s "I told you to scram!"
    n "You leave, just before Vivienne finds Stephanie."
    jump part3_start
