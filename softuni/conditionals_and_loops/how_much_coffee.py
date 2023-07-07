qualified_events = ['coding', 'cat', 'dog', 'movie']
coffee = 0
flag = False
while True:
    event = input()
    if event == "END":
        flag = True
        break

    if event.lower() in qualified_events:
        if event.isupper():
            coffee += 2
        else:
            coffee += 1

    if coffee > 5:
        print("You need extra sleep")
        break
if flag:
    print(coffee)
