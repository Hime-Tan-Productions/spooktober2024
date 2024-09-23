label death_corpse_plant:
    show vivienne angry
    $ renpy.music.set_volume(1.0,0.0,"sound")
    play sound "sword-drawing.mp3" noloop
    n "You hear the garden shears before you see them."
    $ renpy.music.set_volume(0.9,0.0,"nature")
    play nature "stab sound 2.mp3" noloop
    n "The steel blades slice through your neck as easily as snipping a rose from its stem."
    $ renpy.music.set_volume(0.9,0.0,"other")
    play other "vivienne laugh.mp3" noloop
    n "You find out the legend is true that a severed head is still briefly conscious after being decapitated from the body."
    $ renpy.music.set_volume(0.9,0.0,"noise")
    play noise "corpse flower buzz.mp3" noloop
    n "This offers one last fleeting glimpse of the corpse flower."
    $ renpy.music.set_volume(0.9,0.0,"ambience")
    play ambience "stab sound 2.mp3" noloop
    $ renpy.sound.set_volume(0.0,3.0,"death")
    $ renpy.music.set_volume(0.6,3.0,"music")
    play music "garden trip hop esque groove with birds.mp3" loop 
    