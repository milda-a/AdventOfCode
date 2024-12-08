from collections import defaultdict

from read_data import read_in_data

sorted_data = defaultdict(list)
sorted_data["#"] = []
data_len = None
line_len = None


def is_valid(tup):
    return 0 <= tup[0] <= data_len - 1 and 0 <= tup[1] <= line_len - 1

def generate_antinodes(tup1, tup2):
    first = tup1
    second = tup2
    x_diff = first[0] - second[0]
    y_diff = first[1] - second[1]
    antinodes = []
    antinode_a = (first[0] + x_diff, first[1] + y_diff)
    antinode_b = (second[0] - x_diff, second[1] - y_diff)
    while is_valid(antinode_a):
        antinodes.append(antinode_a)
        antinode_a = (antinode_a[0] + x_diff, antinode_a[1] + y_diff)
    while is_valid(antinode_b):
        antinodes.append(antinode_b)
        antinode_b = (antinode_b[0] - x_diff, antinode_b[1] - y_diff)
    for each in antinodes:
        sorted_data['#'].append(each)

def mark(arr):
    if len(arr) == 2:
        generate_antinodes(arr[0], arr[1])
    elif len(arr) < 2:
        return
    else:
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr), 1):
                mark([arr[i], arr[j]])


if __name__ == "__main__":
    data = read_in_data("./data/day8.txt")
    part_1_result = 0
    part_2_result = []

    # part 1
    data_len = len(data)
    line_len = len(data[0])
    for i in range(data_len):
        for j in range(line_len):
            if data[i][j] != ".":
                sorted_data[data[i][j]].append((i, j))
    for key, value in sorted_data.items():
        if key == "#":
            continue
        else:
            mark(value)
    part_1_result = len(set(sorted_data["#"]))
    print("Part 1: ", part_1_result)

    # part 2
    for i in sorted_data.values():
        for j in i:
            part_2_result.append(j)
    print("Part 2: ", len(set(part_2_result)))
