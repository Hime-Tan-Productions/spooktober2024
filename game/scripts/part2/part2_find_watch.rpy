label part2_find_watch:
    $clue_moreno = True
    n "One of these coins looks different from the others."
    n "Hey, this isn't a coin! I recognize this pocket watch from somewhere…"
    n "Even under the water, I can see Moreno's name engraved in the gold."
    n "So he came here before he quit…"
    menu:
        p "Now I wonder if he really quit…"
        "Ask about Moreno.":
            jump part2_moreno
        "Don't ask about Moreno.":
            jump koi_thorns_room