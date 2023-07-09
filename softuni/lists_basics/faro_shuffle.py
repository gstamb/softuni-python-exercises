deck = [x for x in input().split()]
shuffles = int(input())

# deck = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# shuffles = 5

for shuffle in range(shuffles):
    first_part = deck[:len(deck)//2]
    first_part.reverse()
    second_part = deck[len(deck)//2:]
    second_part.reverse()
    for card in range(len(deck)):
        if card % 2 == 0:
            deck[card] = first_part.pop()
        else:
            deck[card] = second_part.pop()
print(deck)
