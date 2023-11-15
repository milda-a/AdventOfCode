from read_data import read_in_data


def solve():
    data = read_in_data("../inputs/day_1.txt")

    # part one ✔
    print(len([x for index, x in enumerate(data) if int(x) > int(data[index - 1])]))

    # part two ✔
    counter = 0
    for i in range(2, len(data)):
        common = int(data[i - 1]) + int(data[i - 2])
        current = common + int(data[i])
        previous = common + int(data[i - 3])
        if current > previous:
            counter += 1
    print(counter)


solve()
