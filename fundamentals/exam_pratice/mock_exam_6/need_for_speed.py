cars = {}

for _ in range(int(input())):
    car, millage, fuel = input().split("|")
    if car not in cars:
        cars[car] = {"Millage": int(millage), "Fuel": int(fuel)}
    else:
        cars[car]["Millage"] = int(millage)
        cars[car]["Fuel"] = int(fuel)

while True:

    instruction = input()

    if instruction == "Stop":
        for car in cars:
            print(f"{car} -> Mileage: {cars[car]['Millage']} kms, Fuel in the tank: {cars[car]['Fuel']} lt.")
        break

    if instruction.startswith("Drive"):
        _, car, distance, fuel = instruction.split(" : ")
        if cars[car]["Fuel"] >= int(fuel):
            cars[car]["Fuel"] -= int(fuel)
            cars[car]["Millage"] += int(distance)
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")

        if cars[car]["Millage"] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]

    elif instruction.startswith("Refuel"):
        _, car, fuel = instruction.split(" : ")
        start = cars[car]["Fuel"]
        if cars[car]["Fuel"] + int(fuel) > 75:
            cars[car]["Fuel"] = 75
        else:
            cars[car]["Fuel"] += int(fuel)
        print(f"{car} refueled with {cars[car]['Fuel'] - start} liters")
    elif instruction.startswith("Revert"):
        _, car, kilometers = instruction.split(" : ")
        if cars[car]["Millage"] - int(kilometers) < 10000:
            cars[car]["Millage"] = 10000
        else:
            cars[car]["Millage"] -= int(kilometers)
            print(f"{car} mileage decreased by {kilometers} kilometers")
