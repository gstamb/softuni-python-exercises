WINNING_SYMBOLS = ['@', '#', '$', '^']


def check_length(tkt: str) -> bool:
    if len(tkt) == 20:
        return True
    else:
        return False


def count_uninterrupted(substring: str) -> tuple:
    current_count = 1
    prev_char = ""
    max_char = ""
    max_cnt = 0
    for char in substring:
        if char == prev_char:
            current_count += 1
            if current_count > max_cnt:
                max_cnt = current_count
                max_char = char
        else:
            prev_char = char
            current_count = 1

    if max_cnt >= 5:
        return max_char, max_cnt


def is_winning(tkt: str) -> tuple:
    min_point = len(tkt) // 2
    part_one = tkt[:min_point]
    part_two = tkt[min_point:]

    left_side = count_uninterrupted(part_one)
    right_side = count_uninterrupted(part_two)

    if (left_side is not None and right_side is not None) \
            and min(left_side[1], right_side[1]) >= 6 \
            and right_side[0] == left_side[0]:
        return left_side[0], min(left_side[1], right_side[1])


tickets = input().split(",")
for ticket in tickets:
    ticket = ticket.strip()
    valid_ticket_len = check_length(ticket)
    if valid_ticket_len:
        winning_ticket = is_winning(ticket)
        if winning_ticket:
            symbol, cnt = winning_ticket
            if cnt == 10:
                if symbol in WINNING_SYMBOLS:
                    print(f'ticket "{ticket}" - {cnt}{symbol} Jackpot!')
                else:
                    print(f'ticket "{ticket}" - no match')
            else:
                if symbol in WINNING_SYMBOLS:
                    print(f'ticket "{ticket}" - {cnt}{symbol}')
                else:
                    print(f'ticket "{ticket}" - no match')
        else:
            print(f'ticket "{ticket}" - no match')

    else:
        print("invalid ticket")
