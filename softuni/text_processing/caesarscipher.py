message = input()
cryptic = [chr(ord(x)+3) for x in message]
print("".join(cryptic))