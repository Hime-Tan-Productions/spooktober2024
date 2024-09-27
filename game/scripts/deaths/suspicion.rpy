label suspicion(dmg, ending=None):
    if dmg > 0 and ending == None:
        call debug("All positive sus increases must have an ending defined!")
        return
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
    