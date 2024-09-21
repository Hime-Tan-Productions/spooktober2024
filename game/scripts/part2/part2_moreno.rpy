label part2_moreno:
    p "I'm sorry if I ask basic questions, Vivienne."
    p "You see, I’m not the first reporter from The Eyewitness to cover this story."
    p "Did my colleague Moreno contact you?"
    menu:
        v "I've never heard such a name!"
        "His pocket watch is in your koi pond.":
            call suspicion(100, "death_koi_pond")
        "Are you sure?":
            call suspicion(100, "death_koi_pond")