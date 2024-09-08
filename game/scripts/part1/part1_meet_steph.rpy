label part1_meet_steph:
    show stephanie conversation1
    p "Someone is working in the greenhouse. Maybe she can answer some of my questions!"
    p "Excuse me!"
    u "Oh hello there! My name is Stephanie."
    jump part1_steph_qs

label part1_steph_qs:
    menu: 
        "How can I help you?"
        "Tell me about the Conservatory.":
            jump steph_ask_greenhouse
        "Ask about Vivienne.":
            jump steph_ask_vivienne
        "Ask about Stephanie.":
            jump steph_ask_herself
        "That's all.":
            hide stephanie
            jump part1_left

label steph_ask_greenhouse:
    p "What can you tell me about the greenhouse?"
    s "Far too many to count. But then, it's not the quantity we are known for. It's the quality. Like our renowned Corpse Plant."
    jump part1_steph_qs

label steph_ask_vivienne:
    p "What can you tell me about Vivienne?"
    show stephanie scared
    s "..."
    p "Stephanie shifts her eyes left and right..."
    show stephanie conversation1
    s "She's wonderful. Couldn't be better. Can we talk about something else?"
    jump part1_steph_qs

label steph_ask_herself:
    p "What is your daily routine like?"
    show stephanie scared
    s "Me? Gosh, I'm so busy taking care of all of the plants! I don't have any time for anything else. I take care of them right up until nightfall."
    show stephanie scared
    p "Stephanie shudders."
    p "What happens at night?"
    s "N... nothing."
    show stephanie conversation1
    jump part1_steph_qs