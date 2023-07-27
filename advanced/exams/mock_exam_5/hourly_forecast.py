def forecast(*args):
    """
    Reads input of variable length and displays cities and weather based on a sorting criteria.
    :param args: Receives a variable number of parameters containing city name and weather outlook category:
    `Sunny` , `Cloudy` , `Rainy`.
    :return: result is a multiline string listing all cities with their respective weather. The list should be sorted:
    displaying cities with Sunny weather first, then cities with Cloudy weather and finally cities with Rainy weather.
    In addition, the string needs to be sorted ascending of city name.
    """
    result_string = ""
    for arg in sorted(args, key=lambda x: (-ord(x[1][1]), x[0])):
        town, weather = arg
        result_string += f"{town} - {weather}\n"
    return result_string


def main():
    print(forecast(
        ("Beijing", "Sunny"),
        ("Hong Kong", "Rainy"),
        ("Tokyo", "Sunny"),
        ("Sofia", "Cloudy"),
        ("Peru", "Sunny"),
        ("Florence", "Cloudy"),
        ("Bourgas", "Sunny")))


if __name__ == "__main__":
    main()
