message = input()

alphas = "".join([x for x in message if not x.isdigit()])
take_list = [int(x) for index, x in enumerate([x for x in message if x.isnumeric()]) if index % 2 == 0]
skip_list = [int(x) for index, x in enumerate([x for x in message if x.isnumeric()]) if index % 2 == 1]

str_build = ""

for index, value in enumerate(take_list):
    take_index = take_list[index]
    skip_index = skip_list[index]

    take_string = alphas[:take_index]
    str_build += take_string
    alphas = alphas[take_index + skip_index:]

print(str_build)
