import math


def center_points(coords):
    x1, y1, x2, y2 = coords
    distance1 = math.sqrt(x1 ** 2 + y1 ** 2)
    distance2 = math.sqrt(x2 ** 2 + y2 ** 2)

    if distance1 < distance2:
        return math.floor(x1), math.floor(y1)
    elif distance1 > distance2:
        return math.floor(x2), math.floor(y2)

    else:
        return math.floor(x1), math.floor(y1)


coordinates = [float(input()) for _ in range(4)]
result = center_points(coordinates)
print(result)
