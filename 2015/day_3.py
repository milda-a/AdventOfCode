import read_data


def part_1():
    input = read_data.read_in_data("inputs/day_3.txt")[0]
    x = 0
    y = 0
    houses = {(x, y): 1}  # x, y coords
    for i in input:
        if i == "^":
            y += 1
        elif i == ">":
            x += 1
        elif i == "v":
            y -= 1
        else:
            x -= 1
        if houses.get((x, y)):
            houses[(x, y)] += 1
        else:
            houses[(x, y)] = 1
    print(len(houses))


def part_2():
    input = read_data.read_in_data("inputs/day_3.txt")[0]
    santa_x, santa_y, robo_x, robo_y = (0, 0, 0, 0)
    houses = {(0, 0): 2}  # x, y coords
    for x, i in enumerate(input):
        if x % 2 == 0:
            if i == "^":
                santa_y += 1
            elif i == ">":
                santa_x += 1
            elif i == "v":
                santa_y -= 1
            else:
                santa_x -= 1
            if houses.get((santa_x, santa_y)):
                houses[(santa_x, santa_y)] += 1
            else:
                houses[(santa_x, santa_y)] = 1
        else:
            if i == "^":
                robo_y += 1
            elif i == ">":
                robo_x += 1
            elif i == "v":
                robo_y -= 1
            else:
                robo_x -= 1
            if houses.get((robo_x, robo_y)):
                houses[(robo_x, robo_y)] += 1
            else:
                houses[(robo_x, robo_y)] = 1
    print(len(houses))


if __name__ == "__main__":
    part_1()
    part_2()
