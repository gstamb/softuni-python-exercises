collection = {}


def piece_exists(song: str) -> bool:
    for composer in collection.keys():
        if song in collection[composer]:
            return composer
    else:
        return None


for initial_pieces in range(int(input())):
    piece, artist, key = input().split("|")
    if artist not in collection:
        collection[artist] = {piece: key}
    else:
        collection[artist][piece] = key

while True:
    instruction = input()
    if instruction == "Stop":
        break

    if instruction.startswith("Add"):
        _, piece, composer, key = instruction.split("|")
        if piece_exists(piece):
            print(f"{piece} is already in the collection!")
        else:
            if composer not in collection:
                collection[composer] = {piece: key}
            else:
                collection[composer][piece] = key
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif instruction.startswith("Remove"):
        _, piece = instruction.split("|")
        composer = piece_exists(piece)
        if composer:
            del collection[composer][piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif instruction.startswith("Change"):
        _, piece, new_key = instruction.split("|")
        composer = piece_exists(piece)
        if composer:
            collection[composer][piece] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for composer, songs in collection.items():
    for song, key in songs.items():
        print(f"{song} -> Composer: {composer}, Key: {key}")