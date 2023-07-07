cnt = int(input())

for _ in range(cnt):
    instruction = int(input())
    if instruction == 88:
        print("Hello")
    elif instruction == 86:
        print("How are you?")
    elif instruction <= 88:
        print('GREAT!')
    elif instruction > 88:
        print('Bye.')
