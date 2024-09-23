label death_vivienne_call_police:
    $ renpy.music.set_volume(0.0,1.0,"music")
    $ renpy.sound.set_volume(0.0,0.0,"other")
    $ renpy.sound.set_volume(0.0,0.0,"noise")
    $ renpy.sound.set_volume(0.0,0.0,"sound")
    $ renpy.music.set_volume(0.0,1.0,"ambience")
    play death "it was you (harsh horror reveal strings).mp3" loop
    $ renpy.sound.set_volume(1.0,0.0,"death")
    $ renpy.music.set_volume(1.0,0.0,"sound")
    $ renpy.music.set_volume(1.0,0.0,"sound")
    play sound "chase-running.mp3" noloop
    n "I rush to the entrance, where I saw a phone."
    $ renpy.sound.set_volume(0.0,1.0,"sound")
    $ renpy.music.set_volume(2.0,0.0,"noise")
    play noise "heels.mp3" noloop
    $ renpy.music.set_volume(0.5,0.0,"other")
    play other "phone dial.mp3" noloop
    n "I hear footsteps behind me. I rush to dial the operator."
    n "But she's too fast."
    $ renpy.music.set_volume(0.0,0.2,"noise")
    v "I'm afraid that I won't be allowing that."
    $ renpy.music.set_volume(0.0,0.2,"other")
    $ renpy.music.set_volume(0.0,0.2,"noise")
    $ renpy.music.set_volume(1.0,0.0,"ambience")
    play ambience "cutting the cord.mp3" noloop
    $ renpy.sound.set_volume(0.4,0.0,"noise")
    play noise "sword-drawing.mp3" noloop
    n "She's cut the phone cable, and she's walking toward me with her shears out..."
    $ renpy.sound.set_volume(1.0,0.0,"sound")
    play sound "stab sound 2.mp3" noloop
    $ renpy.music.set_volume(0.9,0.0,"other")
    play other "death gasp.mp3" noloop
    $ renpy.sound.set_volume(0.0,3.0,"death")
    $ renpy.music.set_volume(0.6,3.0,"music")
    play music "garden trip hop esque groove with birds.mp3" loop 
