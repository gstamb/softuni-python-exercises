days = int(input())
daily_plunder = int(input())
expected_plunder_end = int(input())

plunder_collected = 0
for day in range(1, days + 1):
    plunder_collected += daily_plunder
    if day % 3 == 0:
        plunder_collected += daily_plunder / 2
    if day % 5 == 0:
        plunder_collected *= 0.7

if plunder_collected >= expected_plunder_end:
    print(f"Ahoy! {plunder_collected:.2f} plunder gained.")
else:
    print(f"Collected only {plunder_collected/expected_plunder_end*100:.2f}% of the plunder.")