label suspicion(dmg, ending=None):
    $suspicion += dmg
    if suspicion < 0:
        $suspicion = 0
    if suspicion >= max_suspicion and ending != None:
        $suspicion = max_suspicion
        scene black with fade
        hide screen suspicion with moveouttop
        show vivienne angry_folded
        $renpy.call("" + ending)
        show red_flash
        pause 1
        call screen game_over
    return
    