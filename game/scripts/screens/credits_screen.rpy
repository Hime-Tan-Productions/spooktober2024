screen credits_screen():
    vbox:
        xalign 0.5
        yalign 0.5
        text "[config.name]\nmade for Spooktober 2024\n\nThank you for playing!"
        textbutton _("Credits") action ShowMenu("credits")
        textbutton _("Main Menu") action MainMenu(confirm=False)