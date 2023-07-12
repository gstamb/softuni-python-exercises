phonebook = {}

while True:
    entry = input()
    if entry.isdigit():
        break

    name, phone = entry.split("-")

    # update the phone number if it exists else create
    phonebook[name] = phone

search_request_length = int(entry)
for _ in range(search_request_length):
    search = input()
    if search in phonebook.keys():
        print(f"{search} -> {phonebook[search]}")
    else:
        print(f"Contact {search} does not exist.")
