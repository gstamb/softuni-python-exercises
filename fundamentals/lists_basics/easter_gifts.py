gifts = []
while True:
    cmnd = input()

    if cmnd == "No Money":
        break
    elif cmnd.startswith("OutOfStock"):
        gift_name = cmnd.split()[1]
        if gift_name in gifts:
            while gift_name in gifts:
                index = gifts.index(gift_name)
                gifts[index] = None
    elif cmnd.startswith("Required"):
        gift_name = cmnd.split()[1]
        index = int(cmnd.split()[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_name
    elif cmnd.startswith("JustInCase"):
        gift_name = cmnd.split()[1]
        gifts[-1] = gift_name
    else:
        for gift in cmnd.split():
            gifts.append(gift)

for gift in gifts:
    if gift != None:
        print(gift, end=" ")
