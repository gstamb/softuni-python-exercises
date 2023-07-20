countries = input().split(", ")
capitals = input().split(", ")
countries_capitals = dict(zip(countries, capitals))
for country, capital in countries_capitals.items():
    print(f"{country} -> {capital}")


# can achieve the same a zip by using list comprehension
# test = {countries[i]: capitals[i] for i in range(len(countries))}
# print(test)
