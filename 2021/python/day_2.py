from read_data import read_in_data


def solve():
    data = read_in_data('../inputs/day_2.txt')

    horizontal_position = 0
    depth = 0

    # part one ✔
    for line in data:
        coords = line.split(' ')
        if coords[0] == 'forward':
            horizontal_position += int(coords[1])
        elif coords[0] == 'down':
            depth += int(coords[1])
        else:
            depth -= int(coords[1])
    print(f"hor: {horizontal_position}, dep: {depth}, together: {horizontal_position * depth}")

    horizontal_position = 0
    depth = 0
    aim = 0

    # part two ✔
    for line in data:
        coords = line.split(' ')
        if coords[0] == 'down':
            aim += int(coords[1])
        elif coords[0] == 'up':
            aim -= int(coords[1])
        else:
            horizontal_position += int(coords[1])
            depth += aim * int(coords[1])
    print(f"hor: {horizontal_position}, depth: {depth}, cur aim: {aim}, multiplication: {horizontal_position * depth}")


solve()
