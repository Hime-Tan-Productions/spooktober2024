label suspicion(dmg, ending=None):
    if dmg > 0 and ending == None:
        call debug("All positive sus increases must have an ending defined!") from _call_debug
        return
    if dmg > 0 and suspicion < max_suspicion:
        play sus "sus sound up.mp3" noloop
    elif dmg < 0:
        play sus "sus sound down.mp3" noloop
    $suspicion += dmg
    if suspicion < 0:
        $suspicion = 0
    if suspicion >= max_suspicion and ending != None:
        $suspicion = max_suspicion
        scene black with fade
        hide screen suspicion_bar with moveouttop
        show vivienne angry_folded
        $renpy.call("" + ending)
        show red_flash
        pause 1
        call screen game_over
    return
