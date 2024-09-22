label banana_room:
    scene bg banana_room
    if part == 1:
        if not met_stephanie:
            p "At least the plants are nice here. The people… not so much."
            p "Why do I always feel like trees are trying to tell me something?"
            p "Is something moving in the plants?"
    call screen mansion_interior_banana
