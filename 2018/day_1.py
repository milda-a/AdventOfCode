from read_data import read_in_data


def calculate_frequency_change(array):
    counter = 0
    freq_checks = {}
    found = False
    while not found:
        for num in array:
            counter += num
            if counter not in freq_checks:
                freq_checks[counter] = 1
            else:
                print(f"frequency duplicate found: {counter}")
                found = True
                break
    return counter


if __name__ == "__main__":
    input = [int(x) for x in read_in_data('inputs/day_1.txt')]
    print(calculate_frequency_change(input))
