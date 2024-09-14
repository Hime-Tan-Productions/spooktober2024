screen journal_tabs:
    grid 1 4:
        imagebutton:
            idle "journal_tab"
            foreground Text("Story", style="journal_tab")
            action Call("show_journal")
        imagebutton:
            idle "journal_tab"
            foreground Text("TODO", style="journal_tab")
            action Call("show_journal")
        imagebutton:
            idle "journal_tab"
            foreground Text("People", style="journal_tab")
            action Call("show_journal")
        imagebutton:
            idle "journal_tab"
            foreground Text("Prefs", style="journal_tab")
            action ShowMenu("preferences")

label show_journal:
    call screen journal with moveinleft

label hide_journal:
    hide journal_tabs with moveoutleft

screen journal:
    imagebutton:
        idle "journal"
        foreground Text("TODO: Text appears here as it's unlocked in game. For now, click to close.")
        action Call("hide_journal")
        xpos 500
        ypos 500

style journal_tab:
    vertical True
    xpos 10
    ypos 10
