from read_data import read_in_data
from collections import Counter


def checksum(input):
    exactly_two = 0
    exactly_three = 0

    for line in input:
        counter = Counter(line)
        values = counter.values()
        if 2 in values:
            exactly_two += 1
        if 3 in values:
            exactly_three += 1

    print(exactly_two * exactly_three)

    for value1 in input:
        EXPECTING_MATCH = len(value1) - 1
        for value2 in input:  # double loops are bad mkay
            build_it_up = ""
            if value1 != value2:  # same values are not what we're looking at here
                for i in range(len(value1)):  # index through lines god this is horrible
                    if value1[i] == value2[i]:
                        build_it_up += value1[i]
            if len(build_it_up) == EXPECTING_MATCH:
                print(build_it_up)
                break


if __name__ == "__main__":
    input = read_in_data('inputs/day_2.txt')
    checksum(input)
