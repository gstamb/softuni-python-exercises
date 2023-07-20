wealth = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())


if minimum_wealth * len(wealth) > sum(wealth):
    print("No equal distribution possible")
elif minimum_wealth * len(wealth) == sum(wealth):
    wealth = [minimum_wealth for x in range(len(wealth))]
    print(wealth)
else:
    for index, value in enumerate(wealth):
        if value < minimum_wealth:
            to_add = minimum_wealth - value
            wealth[index] += to_add

            max_wealth = max(wealth)
            index_max_wealth = wealth.index(max_wealth)
            wealth[index_max_wealth] -= to_add
    print(wealth)

