from collections import deque


def make_milkshake(chocolate, milk):
    milkshakes_made = 0
    while milkshakes_made < 5 and chocolate and milk:
        last_chocolate = chocolate.pop()
        first_milk = milk.popleft()
        # need to check whether both or a single value is below zero and append the non-zero back to the queue
        if last_chocolate <= 0 and first_milk <= 0:
            continue
        elif last_chocolate <= 0:
            milk.appendleft(first_milk)
            continue
        elif first_milk <= 0:
            chocolate.append(last_chocolate)
            continue

        # make milkshake if equal
        if last_chocolate == first_milk:
            milkshakes_made += 1
        else:
            # otherwise decrease value of chocolate and return to the queue
            milk.append(first_milk)
            last_chocolate -= 5
            chocolate.append(last_chocolate)
    else:
        return milkshakes_made


def print_results(milkshakes_made, milk, chocolate):
    if milkshakes_made == 5:
        print("Great! You made all the chocolate milkshakes needed!")
    else:
        print("Not enough milkshakes.")

    if chocolate:
        print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
    else:
        print("Chocolate: empty")

    if milk:
        print(f"Milk: {', '.join([str(x) for x in milk])}")
    else:
        print("Milk: empty")


def main():
    chocolate = deque(map(int, input().split(", ")))
    milk = deque(map(int, input().split(", ")))

    milkshakes_made = make_milkshake(chocolate, milk)

    print_results(milkshakes_made, milk, chocolate)


if __name__ == "__main__":
    main()
