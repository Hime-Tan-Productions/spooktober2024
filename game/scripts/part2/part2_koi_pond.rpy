label part2_koi_thorns:
    scene bg koi_thorns with fade
    call screen mansion_interior_koi_thorn

label part2_viv_koi_pond_interview:
    show vivienne conversation
    $flags["p2_viv_koi_pond_int"] = True

    v "This here is the most tranquil part of my greenhouse!"
    v "I have some of the rarest koi species in my pond."
    n "Dew drops cover the lily pads on the water. The dew drops are perfectly round."
    
    menu:
        "Vivienne’s koi pond creeps me out more than it calms me."
        "Is there anything else in the koi pond?":
            v "Why don’t you see for yourself? I’m done with stupid questions!  Stop ruining my peace."
            call suspicion(5, "death_koi_pond")
        "What makes your koi so special?":
            v "My koi are here to keep the peace."
            v "They hide more than you know…"
    jump part2_koi_nice

label part2_koi_nice:
    p "You're right, your pond is very peaceful!"
    menu:
        v "I know! Gives the greenhouse a little something extra."
        "I could stay here all day!":
            v "I hope you’ll be leaving soon."
            call suspicion(5)
        "It seems odd that everything in the greenhouse has something extra.":
            call suspicion(-5)
            v "Certainly! My greenhouse is the world’s best plant collection!"
    jump koi_thorns_room