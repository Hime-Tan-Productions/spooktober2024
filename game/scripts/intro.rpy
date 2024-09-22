label intro:
    scene bg greenhouse_exterior with fade
    play music "ethereal watery ambient atmosphere.mp3" loop
    p "Nice to have a break from the newsroom for now… and the boss yelling at everyone."
    p "I'm upset that Moreno quit without notice too. But I'm not throwing coffee mugs at the secretary!"    
    n "You reach into your pockets for your tape recorder, but remember that Moreno borrowed it and never returned it to you."
    p "Guess I'll have to write my notes down for now."
    n "The Corpse Flower\nBy UX, Associate Managing Editor"

    #$renpy.call("write_in_journal", "Story", "\nCorpse Flower\n\nBy <PC name>, Associate Managing Editor\n")

    p "At least with Moreno gone, I got a promotion! Now if only I'd get a raise too…"
    #$renpy.call("write_in_journal", "Story", "June 21, 1936: corpse flower should bloom tonight. Hundreds of visitors coming to see it.\n")
    p "June 21, 1926: corpse flower should bloom tonight. Hundreds of visitors coming to see it."
    p "Vivienne has been running the greenhouse since her husband died earlier this year."
    p "It's hard to write with my palms so sweaty. Why do I always get so nervous before interviews? I've done hundreds of them."
    p "I just have to talk to the greenhouse owner. This should be a simple story."
    #$renpy.call("write_in_journal", "People", "\nVivienne\nRunning greenhouse since husband died earlier this year")

    call screen mansion_exterior
    p "Guess I'll have to write my notes down for now."