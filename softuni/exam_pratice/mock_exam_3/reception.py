employees_hourly_capacity = [int(input()) for x in range(3)]
requests = int(input())
total_hours = 0
extra_hours = 0
while requests > 0:
    total_hours += 1
    requests -= sum(employees_hourly_capacity)
    if total_hours % 3 == 0 and requests > 0:
        extra_hours += 1

hours_inc_breaks = total_hours + extra_hours
print(f"Time needed: {hours_inc_breaks}h.")
