from collections import deque


def biggest_order(queue: deque) -> int:
    return max(queue)


def service_customers(queue: deque, available_food_amount: int) -> str:
    while available_food_amount > 0:
        if queue:
            order_size = queue.popleft()
            # return item to queue if not enough food
            if order_size > available_food_amount:
                queue.appendleft(order_size)
                break
            available_food_amount -= order_size
        else:
            break

    if queue:
        return f"Orders left: {' '.join([str(x) for x in queue])}"
    else:
        return "Orders complete"


def main():
    available_food = int(input())
    customers = [int(x) for x in input().split()]
    order_of_customers = deque(customers)
    print(biggest_order(order_of_customers))
    print(service_customers(order_of_customers, available_food))


if __name__ == "__main__":
    main()
