from collections import defaultdict
from pprint import pprint

from read_data import read_in_data

if __name__ == "__main__":
    data = read_in_data("./data/day6.txt")
    part_1_result = 0
    part_2_result = 0

    # part 1
    guard_index = None

    # find starting point
    for line_index, each_line in enumerate(data):
        if pos_index := [i for i, x in enumerate(each_line) if x == "^"]:
            guard_index = (line_index, pos_index[0])
            break

    # traverse
    marked_map = data.copy()
    marked_map[guard_index[0]] = (
        marked_map[guard_index[0]][: guard_index[1]]
        + "X"
        + marked_map[guard_index[0]][guard_index[1] + 1 :]
    )
    positions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    blockers = defaultdict(list)

    current_x = guard_index[0]
    current_y = guard_index[1]
    current_position = positions["up"]

    def get_position(x, y):
        if (x, y) == positions["up"]:
            return "up"
        elif (x, y) == positions["right"]:
            return "right"
        elif (x, y) == positions["down"]:
            return "down"
        elif (x, y) == positions["left"]:
            return "left"

    def change_position():
        global current_position
        if current_position == positions["up"]:
            current_position = positions["right"]
        elif current_position == positions["right"]:
            current_position = positions["down"]
        elif current_position == positions["down"]:
            current_position = positions["left"]
        elif current_position == positions["left"]:
            current_position = positions["up"]

    def next_position():
        global current_position
        if current_position == positions["up"]:
            return positions["right"]
        elif current_position == positions["right"]:
            return positions["down"]
        elif current_position == positions["down"]:
            return positions["left"]
        elif current_position == positions["left"]:
            return positions["up"]

    try:
        while True:
            next_x, next_y = (
                current_x + current_position[0],
                current_y + current_position[1],
            )
            if next_x < 0 or next_y < 0:
                raise IndexError
            if data[next_x][next_y] == "#":
                blockers[(next_x, next_y)].append(current_position)
                change_position()
            else:
                marked_map[next_x] = (
                    marked_map[next_x][:next_y] + "X" + marked_map[next_x][next_y + 1 :]
                )
                check_x, check_y = next_position()
                list_to_investigate = []
                if check_x == -1:
                    list_to_investigate = [(i, next_y) for i in range(next_x, -1, -1)]
                elif check_x == 1:
                    list_to_investigate = [
                        (i, next_y) for i in range(next_x, len(data))
                    ]
                elif check_y == -1:
                    list_to_investigate = [(next_x, i) for i in range(next_y, -1, -1)]
                elif check_y == 1:
                    list_to_investigate = [
                        (next_x, i) for i in range(next_y, len(data[next_x]))
                    ]
                if blocker_positions := [
                    i for i in list_to_investigate if i in blockers.keys()
                ]:
                    if next_position() in [blockers[i][0] for i in blocker_positions]:
                        part_2_result += 1
                current_x = next_x
                current_y = next_y
    except IndexError:
        print("Guard left the area!")

    part_1_result = sum([sum([1 for x in line if x == "X"]) for line in marked_map])
    print("Part 1: ", part_1_result)

    # part 2
    print("Part 2: ", part_2_result)
