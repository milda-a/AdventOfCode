import read_data

if __name__ == "__main__":
    input = read_data.read_in_data("inputs/day_1.txt")[0]
    print(0 + input.count("(") - input.count(")"))

    floor = 0

    for i, x in enumerate(input):
        floor = floor + 1 if x == "(" else floor - 1
        if floor == -1:
            print(i + 1)
            break
    print(floor)
