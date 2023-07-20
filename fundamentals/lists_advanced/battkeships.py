ships = [[int(x) for x in input().split()] for points in range(int(input()))]

len_before = len([val for sublist in ships for val in sublist if val == 0])

attacks = [x for x in input().split()]

for attack in attacks:
    x, y = map(int, attack.split("-"))

    if ships[x][y] > 0:
        ships[x][y] -= 1

len_after = len([val for sublist in ships for val in sublist if val == 0])
print(len_after - len_before)

# # 2-D List this will flatten a d2 list
# matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#
# # Nested List Comprehension to flatten a given 2-D matrix
# flatten_matrix = [val for sublist in matrix for val in sublist]