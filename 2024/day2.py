from collections import Counter
from typing import List

from read_data import read_in_data


def is_safe(num1, num2):
    if abs(num1 - num2) <= 3 and num1 != num2:
        return True
    return False


if __name__ == "__main__":
    data = read_in_data("./data/day2.txt")
    data = [[int(x) for x in line.split(" ")] for line in data]

    # part 1
    safe_lines = 0

    for line in data:
        if all(i < j and j - i <= 3 for i, j in zip(line, line[1:])) or all(
            i > j and i - j <= 3 for i, j in zip(line, line[1:])
        ):
            safe_lines += 1

    print("safe lines for part 1: ", safe_lines)

    # part 2

    def non_increasing_pairs(ar: List):
        pairs = len(ar) - 1
        increasing_pairs = sum(i < j and j - i <= 3 for i, j in zip(ar, ar[1:]))
        if increasing_pairs == pairs:
            return 0
        return pairs - increasing_pairs

    def non_decreasing_pairs(ar: List):
        pairs = len(ar) - 1
        decreasing_pairs = sum(i > j and i - j <= 3 for i, j in zip(ar, ar[1:]))
        if pairs == decreasing_pairs:
            return 0
        return pairs - decreasing_pairs

    safe_lines = 0
    for line in data:
        non_inc = non_increasing_pairs(line)
        non_dec = non_decreasing_pairs(line)
        if non_inc == 0 or non_dec == 0:
            safe_lines += 1
            continue
        elif non_inc > 2 and non_dec > 2:
            # multiple fails
            continue
        else:
            # handle the single error
            if non_inc <= 2:
                problem_pair = [
                    item
                    for item in enumerate(zip(line, line[1:]))
                    if item[1][1] - item[1][0] > 3 or item[1][0] >= item[1][1]
                ][0]
                if problem_pair[0] == 0 and non_increasing_pairs(line[1:]) == 0:
                    safe_lines += 1
                elif (
                    non_increasing_pairs(
                        line[: problem_pair[0]] + line[problem_pair[0] + 1 :]
                    )
                    == 0
                ):
                    safe_lines += 1
                elif (
                    problem_pair[0] + 1 <= len(line) - 1
                    and non_increasing_pairs(
                        line[: problem_pair[0] + 1] + line[problem_pair[0] + 2 :]
                    )
                    == 0
                ):
                    safe_lines += 1
            elif non_dec <= 2:
                problem_pair = [
                    item
                    for item in enumerate(zip(line, line[1:]))
                    if item[1][0] - item[1][1] > 3 or item[1][0] <= item[1][1]
                ][0]
                if problem_pair[0] == 0 and non_decreasing_pairs(line[1:]) == 0:
                    safe_lines += 1
                elif (
                    non_decreasing_pairs(
                        line[: problem_pair[0]] + line[problem_pair[0] + 1 :]
                    )
                    == 0
                ):
                    safe_lines += 1
                elif (
                    problem_pair[0] + 1 <= len(line) - 1
                    and non_decreasing_pairs(
                        line[: problem_pair[0] + 1] + line[problem_pair[0] + 2 :]
                    )
                    == 0
                ):
                    safe_lines += 1
    print("safe lines for part 2: ", safe_lines)
