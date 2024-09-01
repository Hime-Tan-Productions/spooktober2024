label tutorial_conversation:
    e "Let's try out a branching conversation! What would you like to know about?"
    menu:
        "Tell me about your favorite book.":
            jump conv
        
        "I'm done.":
            jump start