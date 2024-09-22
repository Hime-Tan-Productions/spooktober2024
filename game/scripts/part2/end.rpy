label part2_end_ask:
        if int_corpse_flower:
            menu:
                n "The viewing will begin soon. Are you ready?"
                "Yes":
                    jump part3_start
                "No":
                    pass

label part2_end:
    v "My beautiful corpse plant shall bloom soon!"
    jump part3_start