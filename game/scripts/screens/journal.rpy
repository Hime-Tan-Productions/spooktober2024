screen journal_tabs:
    grid 1 4:
        imagebutton:
            idle "journal_tab"
            foreground Text("Story", style="journal_tab")
            action ShowMenu("journal", _transition=moveinleft, tab="Story")
        imagebutton:
            idle "journal_tab"
            foreground Text("TODO", style="journal_tab")
            action ShowMenu("journal", _transition=moveinleft, tab="Todo")
        imagebutton:
            idle "journal_tab"
            foreground Text("People", style="journal_tab")
            action ShowMenu("journal", _transition=moveinleft, tab="People")
        imagebutton:
            idle "journal_tab"
            foreground Text("Prefs", style="journal_tab")
            action ShowMenu("preferences")

label hide_journal:
    hide journal_tabs with moveoutleft
    return

screen journal:
    modal True
    text tab
    fixed:
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 800
        image "journal"
        vbox:
            text "Tab: " + tab

            if tab == "Story":
                for item in journal_story:
                    text item
                pass
            if tab == "TODO":
                for item in journal_todo:
                    text item
                pass
            if tab == "People":
                for item in journal_people:
                    text item

            imagebutton:
                idle "left"
                action Call("hide_journal")

style journal_tab:
    vertical True
    xpos 10
    ypos 10
