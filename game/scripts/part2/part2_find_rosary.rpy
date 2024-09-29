label part2_find_rosary:
    $clue_nun = True
    n "There is a rosary on the floor. Its beads are caked with a grimy red substance."
    n "The sign here says the crown of thorns plant is from the personal collection of Sister Mary Garcia."
    n "That name sounds familiar! Same as a missing person cold case I reported on last year."
    menu:
        p "How did this end up here…"
        "Ask about Sister Garcia.":
            play vo "voices/Vivienne/viv_5_yoshi_harried.mp3" noloop
            show vivienne angry_folded
            jump part2_sister_garcia
        "Don't ask about Sister Garcia.":
            jump koi_thorns_room