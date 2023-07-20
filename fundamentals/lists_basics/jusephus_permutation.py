soldiers = [int(x) for x in input().split()]
cnt = int(input())
order_of_execution = []
while len(soldiers) > 0:
    index = len(soldiers)
    to_remove = (cnt % index) - 1
    order_of_execution.append(soldiers.pop(to_remove))
    if to_remove == -1:
        soldiers = soldiers
    else:
        left = soldiers[:to_remove]
        right = soldiers[to_remove:]
        soldiers = right + left

print(f"[{','.join(str(x) for x in order_of_execution)}]")

# 10 5 65 104 1 0 2
# 5 65 104 1 0 2      10
# 104 1 0 2 5     10 65
# 2 5 104 1     10 65 0
# 2 5 104      10 65 0 1
# 104 2      10 65 0 1 5
# 104       10 65 0 1 5 2
