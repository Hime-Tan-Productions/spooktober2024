label suspicion(dmg, ending=None):
    $suspicion += dmg
    if suspicion < 0:
        $suspicion = 0
    if suspicion >= max_suspicion and ending != None:
        $suspicion = max_suspicion
        $renpy.call("" + ending)
        scene black with fade
        p "You die."
        while True:
            pause
            $MainMenu()()
    return
    