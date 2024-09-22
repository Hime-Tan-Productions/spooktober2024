label intro:
    scene bg greenhouse_exterior with fade
    play music "ethereal watery ambient atmosphere.mp3" loop
    $ renpy.music.set_volume(0.42,0,"music")
    $ renpy.music.set_volume(0.1,14.0,"music")
    $ renpy.sound.set_volume(0.06,0,"sound")
    play sound "intro sfx 3.mp3"
    p "Nice to have a break from the newsroom for now….and the boss yelling at everyone."
    p "I’m upset that Moreno quit without notice too. But I’m not throwing coffee mugs at the secretary!" 
    play nature "ducks 2.mp3" loop
    $ renpy.sound.set_volume(0.5,0,"nature")   
    p "Guess I’ll have to write my notes down for now."
    #$renpy.call("write_in_journal", "Story", "\nCorpse Flower\n\nBy <PC name>, Associate Managing Editor\n")

    p "At least with Moreno gone, I got a promotion! Now if only I’d get a raise too…"
    #$renpy.call("write_in_journal", "Story", "June 21, 1936: corpse flower should bloom tonight. Hundreds of visitors coming to see it.\n")
    $ renpy.sound.set_volume(0.0,1.0,"sound")

    p "It’s hard to write with my palms so sweaty. Why do I always get so nervous before interviews? I’ve done hundreds of them."
    p "I just have to talk to the greenhouse owner. This should be a simple story."
    #$renpy.call("write_in_journal", "People", "\nVivienne\nRunning greenhouse since husband died earlier this year")

    call screen mansion_exterior
    p "Guess I’ll have to write my notes down for now."
