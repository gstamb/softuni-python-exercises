requests = int(input())
parking_registration = {}

for _ in range(requests):
    request = input().split()
    if len(request) == 2:
        name = request[1]
        if name not in parking_registration:
            print(f"ERROR: user {name} not found")
        else:
            parking_registration.pop(name)
            print(f"{name} unregistered successfully")
    else:
        name = request[1]
        plate_num = request[2]
        if name in parking_registration:
            print(f"ERROR: already registered with plate number {plate_num}")
        else:
            parking_registration[name] = plate_num
            print(f"{name} registered {plate_num} successfully")

for key, value in parking_registration.items():
    print(f"{key} => {value}")

