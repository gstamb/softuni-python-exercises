best_snowball = 0
snowball_weight = 0
snowball_velocity = 0
snowball_quality = 0
for snowball in range(int(input())):
    weight = int(input())
    velocity = int(input())
    quality = int(input())

    score = (weight / velocity) ** quality

    if score > best_snowball:
        best_snowball = score
        snowball_weight = weight
        snowball_velocity = velocity
        snowball_quality = quality


print(f"{snowball_weight} : {snowball_velocity} = {best_snowball:.0f} ({snowball_quality})")


