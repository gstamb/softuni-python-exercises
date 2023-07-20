import re

destinations = input()
travel_points = 0
travel_stops = []
pattern = "(=(?:[A-Z][a-zA-Z]{2,})=|\/(?:[A-Z][a-zA-Z]{2,})\/)"
matches = re.findall(pattern, destinations)

for match in matches:
    travel_stop = match.strip("=").strip("/")
    travel_points += len(travel_stop)
    travel_stops.append(travel_stop)

print("Destinations: {0}".format(", ".join(travel_stops)))
print(f"Travel Points: {travel_points}")
