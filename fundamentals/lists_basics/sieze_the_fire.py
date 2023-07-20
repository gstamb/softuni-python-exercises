HIGH = range(81, 126)
MEDIUM = range(51, 81)
LOW = range(1, 51)

fires = [x for x in input().split("#")]
water = int(input())
effort = 0
print("Cells:")
for fire in fires:
    intensity, value = fire.split(" = ")
    value = int(value)
    if intensity == "High":
        if value in HIGH and water >= value:
            water -= value
            effort += value * 0.25
            print(f" - {value}")
    elif intensity == "Medium":
        if value in MEDIUM and water >= value:
            water -= value
            effort += value * 0.25
            print(f" - {value}")
    elif intensity == "Low":
        if value in LOW and water >= value:
            water -= value
            effort += value * 0.25
            print(f" - {value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {effort * 4:.0f}")
