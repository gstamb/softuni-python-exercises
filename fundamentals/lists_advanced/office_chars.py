def is_enough(room, indx):
    chars, guests = room.split()
    if len(chars) < int(guests):
        more_chairs_needed = int(guests) - len(chars)
        return f"{more_chairs_needed} more chairs needed in room {indx + 1}"
    else:
        return


def excess_chairs(room):
    chars, guests = room.split()
    spare = len(chars) - int(guests)
    return spare


rooms = int(input())
chars_visitors = [input() for x in range(rooms)]
enough_chairs = [is_enough(room, index) for index, room in enumerate(chars_visitors)]
filtered_enough_chairs = [x for x in enough_chairs if x is not None]
if filtered_enough_chairs:
    print("\n".join(filtered_enough_chairs))
else:
    spare_chars = [excess_chairs(x) for x in chars_visitors]
    print(f"Game On, {sum(spare_chars)} free chairs left")
