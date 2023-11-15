from read_data import read_in_data


def solve():
    data = read_in_data("../inputs/day_3.txt")

    # part one ✔
    indexes = {}
    for line in data:
        for index, value in enumerate(line):
            if index not in indexes:
                indexes[index] = {"zero_counter": 0, "ones_counter": 0}
            else:
                if int(value) == 0:
                    indexes[index]["zero_counter"] += 1
                else:
                    indexes[index]["ones_counter"] += 1

    gamma = []
    epsilon = []

    for item in indexes.values():
        if item["zero_counter"] > item["ones_counter"]:
            gamma.append("0")
            epsilon.append("1")
        else:
            gamma.append("1")
            epsilon.append("0")

    gamma_string = "".join(gamma)
    epsilon_string = "".join(epsilon)

    product = int(gamma_string, 2) * int(epsilon_string, 2)
    print(product)

    # part two ✔
    oxygen_generator_data = data.copy()
    co2_scrubber_data = data.copy()
    global_index_tracker = 0

    def ones_and_zeroes(input_list, index):
        zero_count = 0
        one_count = 0
        for line in input_list:
            if line[index] == "1":
                one_count += 1
            else:
                zero_count += 1
        return zero_count, one_count

    while global_index_tracker < len(data[0]):
        o2_zero, o2_one = ones_and_zeroes(oxygen_generator_data, global_index_tracker)
        co2_zero, co2_one = ones_and_zeroes(co2_scrubber_data, global_index_tracker)

        if o2_zero > o2_one:
            for line in oxygen_generator_data.copy():
                if line[global_index_tracker] == "1" and len(oxygen_generator_data) > 1:
                    oxygen_generator_data.remove(line)
        else:
            for line in oxygen_generator_data.copy():
                if line[global_index_tracker] == "0" and len(oxygen_generator_data) > 1:
                    oxygen_generator_data.remove(line)

        if co2_one >= co2_zero:
            for line in co2_scrubber_data.copy():
                if line[global_index_tracker] == "1" and len(co2_scrubber_data) > 1:
                    co2_scrubber_data.remove(line)
        else:
            for line in co2_scrubber_data.copy():
                if line[global_index_tracker] == "0" and len(co2_scrubber_data) > 1:
                    co2_scrubber_data.remove(line)

        # increase global index
        global_index_tracker += 1

    print(oxygen_generator_data, co2_scrubber_data)
    print(int(oxygen_generator_data[0], 2) * int(co2_scrubber_data[0], 2))


solve()
