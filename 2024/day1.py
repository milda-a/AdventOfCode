from read_data import read_in_data
from collections import Counter

if __name__ == "__main__":
    data = read_in_data("./data/day1.txt")
    left = []
    right = []
    data = [x.split("   ") for x in data]
    for x in data:
        left.append(int(x[0]))
        right.append(int(x[1]))

    # part 1

    sorted_left = sorted(left)
    sorted_right = sorted(right)

    diff = 0
    for i in range(len(left)):
        diff += abs(sorted_left[i] - sorted_right[i])

    print("part 1: ", diff)

    # part 2

    total_similarity = 0

    counter = Counter(right)
    counter = dict(counter)

    for item in left:
        total_similarity += counter.get(item, 0) * item

    print("part 2: ", total_similarity)
