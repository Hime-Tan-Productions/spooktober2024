label death_koi_pond:
    $ renpy.music.set_volume(1.0,0.0,"sound")
    play sound "drowning.mp3" noloop
    n  "Vivienne’s grasp is tight around your neck as she shoves your head in the koi pond."
    n "You find yourself face to face with her special koi.J"
    n "Its unflinching black eyes are the last thing you ever see as you fight for air until your body becomes limp."
    play ambience "bubbles.mp3" noloop
    $ renpy.sound.set_volume(0.0,3.0,"death")
    $ renpy.sound.set_volume(0.0,3.0,"sound")
    $ renpy.music.set_volume(0.6,3.0,"music")
    play music "garden trip hop esque groove with birds.mp3" loop 
