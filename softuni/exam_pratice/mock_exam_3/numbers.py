input_arr = [int(x) for x in input().split()]
avg = sum(input_arr) / len(input_arr)
gt_avg = sorted([x for x in input_arr if x > avg], reverse=True)[:5]
if gt_avg:
    print(" ".join([str(x) for x in gt_avg]))
else:
    print("No")
