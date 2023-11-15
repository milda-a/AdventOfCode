import read_data
from string import ascii_lowercase


def get_pairs(the_string):
    return [
        checked_value + the_string[index + 1]
        for index, checked_value in enumerate(the_string)
        if index < len(the_string) - 1
    ]


if __name__ == "__main__":
    input = read_data.read_in_data("inputs/day_5.txt")
    totes = 0
    for current_string in input:
        bads = sum(map(current_string.count, ["ab", "cd", "pq", "xy"]))
        vowels = sum(map(current_string.count, "aieou"))
        repeats = sum(map(current_string.count, [x + x for x in ascii_lowercase]))
        if bads == 0 and vowels >= 3 and repeats >= 1:
            totes += 1
    print(totes)

    goodish = []
    good = []
    for current_string in input:
        pairs = get_pairs(current_string)
        pair_frequency = list(map(current_string.count, pairs))
        for index in range(len(pair_frequency) - 1):
            if pair_frequency[index] > 1 and pairs[index] != pairs[index + 1]:
                goodish.append(current_string)
                break
    for current_string in goodish:
        for index in range(len(current_string) - 2):
            if current_string[index] == current_string[index + 2]:
                good.append(current_string)
                break
    print(len(good))
