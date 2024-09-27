screen debug_screen():
    zorder 100
    hbox:
        textbutton "Sus 0":
            action Call("debug_sus_min")
        textbutton "Sus 100":
            action Call("debug_sus_max")
