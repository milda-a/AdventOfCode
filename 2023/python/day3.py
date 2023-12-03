from collections import defaultdict

import read_data


def part_1():
    total = 0
    input = read_data.read_in_data("../inputs/day3.txt")
    input_amended = [x + "." for x in input]
    input_unique = [set(line) for line in input_amended]
    symbols = [
        [x for x in each_set if not x.isdigit() and x != "."]
        for each_set in input_unique
    ]
    all_symbols = []
    for i in symbols:
        all_symbols += i
    all_symbols = list(set(all_symbols))

    for y, line in enumerate(input_amended):
        seeking_digits = ""
        for x, each_char in enumerate(line):
            if each_char.isdigit():
                seeking_digits += each_char
            else:
                if seeking_digits:
                    for k in range(max(y - 1, 0), min(y + 2, len(input_amended))):
                        for l in range(
                            max(x - len(seeking_digits) - 1, 0), min(x + 1, len(line))
                        ):
                            if input_amended[k][l] in all_symbols:
                                total += int(seeking_digits)
                    seeking_digits = ""
    print(total)


def part_2():
    input = read_data.read_in_data("../inputs/day3.txt")
    gears = defaultdict(list)
    input_amended = [
        x + "." for x in input
    ]  # to not deal with end of line numbers when iteration runs out
    for y, line in enumerate(input_amended):
        seeking_digits = ""
        for x, each_char in enumerate(line):
            if each_char.isdigit():
                seeking_digits += each_char
            else:
                if seeking_digits:
                    for k in range(max(y - 1, 0), min(y + 2, len(input_amended))):
                        for l in range(
                            max(x - len(seeking_digits) - 1, 0), min(x + 1, len(line))
                        ):
                            if input_amended[k][l] == "*":
                                gears[(k, l)].append(int(seeking_digits))
                seeking_digits = ""

    print(sum([gears[k][0] * gears[k][1] for k in gears if len(gears[k]) == 2]))


if __name__ == "__main__":
    part_1()
    part_2()
