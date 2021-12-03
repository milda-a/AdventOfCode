from read_data import read_in_data


def solve():
    # part one ✔
    indexes = {}
    data = read_in_data('../inputs/day_3.txt')
    for line in data:
        for index, value in enumerate(line):
            if index not in indexes:
                indexes[index] = {'zero_counter': 0, 'ones_counter': 0}
            else:
                if int(value) == 0:
                    indexes[index]['zero_counter'] += 1
                else:
                    indexes[index]['ones_counter'] += 1

    gamma = []
    epsilon = []

    for item in indexes.values():
        if item['zero_counter'] > item['ones_counter']:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')

    gamma_string = "".join(gamma)
    epsilon_string = "".join(epsilon)

    product = int(gamma_string, 2) * int(epsilon_string, 2)
    print(product)


solve()
