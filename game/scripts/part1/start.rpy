label part1_start:
    $part = 1
    scene bg koi_thorns
    n "The greenhouse welcomes you with a strong scent of vanilla, plus a hint of death. Must be the corpse flower…"
    call screen mansion_interior_koi_thorn

label part1_main:
    jump koi_thorns_room
