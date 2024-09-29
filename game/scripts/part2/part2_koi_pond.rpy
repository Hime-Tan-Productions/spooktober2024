label part2_koi_thorns:
    scene bg koi_thorns with fade
    call screen mansion_interior_koi_thorn

label part2_viv_koi_pond_interview:
    show vivienne happy_armup
    $int_koi_pond = True
    play vo "voices/Vivienne/yoshi_ahh.mp3" noloop
    v "This here is the most tranquil part of my greenhouse!"
    v "I have some of the rarest koi species in my pond."
    show vivienne neutral_folded
    n "Dew drops cover the lily pads on the water. The dew drops are perfectly round."
    menu:
        
        n "Vivienne's koi pond creeps me out more than it calms me."
        "Is there anything else in the koi pond?":
            show vivienne happy_folded
            play vo "voices/Vivienne/viv_2_yoshi_groan.mp3" noloop
            v "Why don't you see for yourself? I'm done with stupid questions!  Stop ruining my peace."
            call suspicion(25, "death_koi_pond")
        "What makes your koi so special?":
            call suspicion(-10)            
            show vivienne neutral_folded_mouthopen
            v "My koi are here to keep the peace."
            show vivienne angry_folded
            play vo "voices/Vivienne/viv_2_yoshi_normal_2.mp3" noloop
            v "They hide more than you know…"
    jump part2_koi_nice

label part2_koi_nice:
    n "What is this woman on about? No wonder no one else wanted to cover this story!"
    n "Better pretend I don't notice how odd she's acting."
    show vivienne neutral_folded
    p "You're right, your pond is very peaceful!"
    show vivienne happy_armup
    play vo "voices/Vivienne/yoshi_short_laugh.mp3" noloop
    menu:
        v "I know! Gives the greenhouse a little something extra."
        "I could stay here all day!":
            call suspicion(25, "death_koi_pond")
            show vivienne angry_armup
            play vo "voices/Vivienne/viv_2_yoshi_tired.mp3" noloop
            v "I hope you'll be leaving soon."
        "It seems odd that everything in the greenhouse has something extra.":
            call suspicion(-10)
            show vivienne happy_folded
            play vo "voices/Vivienne/yoshi_short_laugh_3.mp3" noloop
            v "Certainly! My greenhouse is the world's best plant collection!"
    jump koi_thorns_room