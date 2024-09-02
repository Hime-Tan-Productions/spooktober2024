label tutorial_conversation:
    scene bg_busstop
    menu:
        e "Let's try out a branching conversation! What would you like to know about?"
        "Tell me about your favorite book.":
            jump conv
        "Tell me a story.":
            jump conv_story
        "Tell me a joke.":
            jump conv_joke        
        "That's it for now.":
            jump tutorial