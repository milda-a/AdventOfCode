from collections import defaultdict
from time import time
from read_data import read_in_data
from itertools import product
import operator


def calculate(arr):
    if len(arr) == 2:
        return operators.get(arr[-1][0])(int(arr[0]), int(arr[1][1:]))
    return calculate([calculate(arr[:-1]), arr[-1]])


operators = {
    "+": operator.add,
    "*": operator.mul,
    "|": lambda x, y: f"{x}{y}",
}

if __name__ == "__main__":
    start = time()
    data = read_in_data("./data/day7.txt")
    mapped_data = defaultdict(list)
    part_1_result = 0
    part_2_result = 0

    # part 1
    for each_line in data:
        key, value = each_line.split(": ")
        mapped_data[int(key)] = value.split(" ")

    for key, value in mapped_data.items():
        possible_permutations = list(product(["*", "+", "|"], repeat=len(value) - 1))
        for permutation in possible_permutations:
            string_to_eval = [
                f"{permutation[i]}{value[i+1]}" for i in range(len(permutation))
            ]
            string_to_eval.insert(0, value[0])
            calculated = calculate(string_to_eval)
            if int(calculated) == key:
                part_1_result += key
                break

    print("Part 1: ", part_1_result)

    # part 2
    print("Part 2: ", part_2_result)
    end = time()
    elapsed = end - start
    elapsed_minutes = elapsed // 60
    elapsed_seconds = elapsed % 60
    print(f"Time: {elapsed_minutes} minutes and {elapsed_seconds} seconds")
