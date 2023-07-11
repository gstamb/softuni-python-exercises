base_list = [int(x) for x in input().split(", ")]
max_element = max(base_list)

for i in range(10, max_element+10, 10):
    print(f"Group of {i}'s: {[x for x in base_list if i-10 < x <= i ]}")



