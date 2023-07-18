import re

inventory = input()
required_calories = 2000
total_available_calories = 0
available_food = []

pattern = "#([A-Za-z ]+)#(\d{2}/\d{2}/\d{2})#(\d+)#|\|([A-Za-z ]+)\|(\d{2}/\d{2}/\d{2})\|(\d{1,4})\|"
matches = re.findall(pattern, inventory)
for match in matches:
    data_cleaning = [x for x in match if x != ""]
    product, date, calories = data_cleaning
    total_available_calories += int(calories)

    string = f"Item: {product}, Best before: {date}, Nutrition: {int(calories)}"
    available_food.append(string)

print(f"You have food to last you for: {total_available_calories // required_calories} days!")
for food in available_food:
    print(food)
