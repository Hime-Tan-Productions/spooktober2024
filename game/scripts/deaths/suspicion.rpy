label suspicion(dmg, ending=None):
    $suspicion += dmg
    if suspicion < 0:
        $suspicion = 0
    if suspicion >= max_suspicion and ending != None:
        $suspicion = max_suspicion
        scene black with fade
        $renpy.call("" + ending)
        scene game_over with fade
        centered "Game Over"
        pause
        call screen game_over
    return
    