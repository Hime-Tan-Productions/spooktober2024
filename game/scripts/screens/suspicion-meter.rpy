screen suspicion_bar():
    zorder 100
    vbox:
        xalign 0.95 yalign 0.01
        xmaximum 400
        ymaximum 25   
        bar value AnimatedValue(suspicion, max_suspicion, delay=1.0):

            right_bar Frame("images/suspicion-meter/suspicion_bg.png", 100, 100)
            left_bar Frame("images/suspicion-meter/suspicion_fg.png", 100, 100)
        text "{color=#FF0000}Suspicion{/color}" at truecenter


