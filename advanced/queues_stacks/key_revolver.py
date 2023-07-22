from collections import deque


def shoot_lock(locks: deque, bullets: deque):
    """ Checks if a bullet can shoot a lock and prints `Ping`, `Bang` respectively
        Bullet, Lock drawn from the queues.
    """
    lock = locks.popleft()
    bullet = bullets.pop()
    if lock >= bullet:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)


def main():
    price_bullet = int(input())
    size_gun_barrel = int(input())
    bullets = deque([int(x) for x in input().split()])
    locks = deque([int(x) for x in input().split()])
    value_intelligence = int(input())

    bullets_used = 0
    while locks and bullets:
        shoot_lock(locks, bullets)
        bullets_used += 1

        # print reload message only if there are bullets left
        if bullets:
            if bullets_used % size_gun_barrel == 0:
                print("Reloading!")

    if locks:
        print(f"Couldn't get through. Locks left: {len(locks)}")
    else:
        earned = value_intelligence - (bullets_used * price_bullet)
        print(f"{len(bullets)} bullets left. Earned ${earned}")


if __name__ == "__main__":
    main()
