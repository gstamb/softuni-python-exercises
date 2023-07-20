import math

number_of_ppl = int(input())
elevator_capacity = int(input())

trips_required = math.ceil(number_of_ppl / elevator_capacity)
print(trips_required)