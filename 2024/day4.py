from read_data import read_in_data
import re
from pprint import pprint


def populate_diagonal_data(original_array, reverse=False):
    # diagonal data
    diag_data = [[] for i in range(len(original_array) * 2 - 1)]
    if reverse:
        for x in range(len(original_array)):
            for y in range(len(original_array) - 1, -1, -1):
                diag_data[x - y + len(original_array) - 1].append(str(original_array[x][y]))
        return ["".join(x) for x in diag_data]
    else:
        for y in range(len(original_array)):
            for x in range(len(original_array)):
                diag_data[y + x].append(str(original_array[x][y]))
        return ["".join(x) for x in diag_data]

def find_all_occurrences(reg, array):
    found = 0
    for each_line in array:
        found += len(re.findall(reg, each_line))
    return found

def check_chunky(chunk):
    diag = populate_diagonal_data(chunk)
    rev = populate_diagonal_data(chunk, reverse=True)
    if find_all_occurrences("(MAS)", diag) > 0 or find_all_occurrences("(SAM)", diag) > 0:
        if find_all_occurrences("(MAS)", rev) > 0 or find_all_occurrences("(SAM)", rev) > 0:
            return True
    return False

if __name__ == '__main__':

    data = read_in_data('./data/day4.txt')
    part_1_result = 0
    part_2_result = 0

    # part 1

    # left to right and back
    part_1_result += find_all_occurrences("(XMAS)", data)
    part_1_result += find_all_occurrences("(SAMX)", data)

    # up and down
    up_and_down_data = ["".join([data[i][j] for i in range(len(data))]) for j in range(len(data))]
    part_1_result += find_all_occurrences("(XMAS)", up_and_down_data)
    part_1_result += find_all_occurrences("(SAMX)", up_and_down_data)

    diagonal_data = populate_diagonal_data(data)
    reversed_diagonal = populate_diagonal_data(data, reverse=True)
    part_1_result += find_all_occurrences("(XMAS)", diagonal_data)
    part_1_result += find_all_occurrences("(SAMX)", diagonal_data)
    part_1_result += find_all_occurrences("(XMAS)", reversed_diagonal)
    part_1_result += find_all_occurrences("(SAMX)", reversed_diagonal)

    print('Part 1: ', part_1_result)

    # part 2
    for x in range(len(data) - 2):
        for y in range(len(data) - 2):
            chunk = [y[x:x + 3] for y in data[y:y + 3]]
            if check_chunky(chunk):
                part_2_result += 1
            continue

    print('Part 2: ', part_2_result)
