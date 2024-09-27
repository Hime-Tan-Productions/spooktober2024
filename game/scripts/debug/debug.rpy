label debug(error):
    $renpy.notify("Encountered an error: %(error)s")
    pause

label debug_sus_max:
    $suspicion = max_suspicion
    return

label debug_sus_min:
    $suspicion = 0
    return