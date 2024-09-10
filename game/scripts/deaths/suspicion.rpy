label suspicion(dmg, ending=None):
    if ending == None and dmg > 0:
        call debug("suspicion has dmg of {dmg} but no ending. This should not happen.")
    $suspicion += dmg
    if suspicion < 0:
        $suspicion = 0
    if suspicion >= max_suspicion:
        $suspicion = max_suspicion
        $renpy.call("" + ending)
        scene black with fade
        p "You die."
        while True:
            pause
            $MainMenu()()
    return
    