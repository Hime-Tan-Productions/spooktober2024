label death_banana:
    show vivienne angry
    v "Why don't you try one of the bananas? They're wonderful!"
    menu:
        "I don't like bananas.":
            v "Unfortunately, you don't have a choice."
            call death_banana_cont
        "I'd love to!":
            v "More food for my sweet girl."
            call death_banana_cont


label death_banana_cont:
    n "Vivienne shoves a poisoned banana in your mouth. As you swallow the sweet fruit, your throat quickly asphyxiates."
    n "The potassium from the banana does not prevent muscle cramps as your body seizures until it never moves again."
