import read_data

if __name__ == "__main__":
    input = read_data.read_in_data("../inputs/day1.txt")

    # part one
    numbers = [[x for x in y if x.isdigit()] for y in input]
    print(sum([int("".join([x[0], x[-1]])) for x in numbers]))

    # part two
    words_to_num = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    all_numbers = []
    for index_for_string, value in enumerate(input):
        all_numbers.append([])
        for index, each_char in enumerate(value):
            if each_char.isdigit():
                all_numbers[index_for_string].append(each_char)
            else:
                for j in words_to_num.keys():
                    if value[index:].startswith(j):
                        all_numbers[index_for_string].append(words_to_num[j])
                        break
    print(sum([int("".join([x[0], x[-1]])) for x in all_numbers]))
