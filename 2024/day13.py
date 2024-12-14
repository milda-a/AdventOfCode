from time import time

from read_data import read_in_data

results = 0


if __name__ == "__main__":
    start = time()
    data = read_in_data("./data/day13.txt")
    part_1_result = 0
    part_2_result = 0

    # part 1
    A_TOKEN = 3
    B_TOKEN = 1
    increases = {"A": {"x": 0, "y": 0}, "B": {"x": 0, "y": 0}}
    prize = {"x": 0, "y": 0}

    def how_many_increases(current_x, current_y, increase_x, increase_y):
        x_by = (prize["x"] - current_x) // increase_x
        y_by = (prize["y"] - current_y) // increase_y
        if x_by > 1 and y_by > 1:
            return min(x_by, y_by)
        return 1

    def moves(x, y, last_increased, last_decreased, a_by, b_by):
        if x == prize["x"] and y == prize["y"]:
            # match
            global results
            outcome = a_by * A_TOKEN + b_by * B_TOKEN
            results = outcome if results == 0 else min(outcome, results)
        else:
            # not yet equal
            if (
                x + increases["A"]["x"] <= prize["x"]
                and y + increases["A"]["y"] <= prize["y"]
                and a_by < 100
                and last_decreased != "A"
            ):
                # increase in A would not overshoot
                increase_by = how_many_increases(
                    x, y, increases["A"]["x"], increases["A"]["y"]
                )
                a_by += increase_by
                moves(
                    x + increases["A"]["x"] * increase_by,
                    y + increases["A"]["y"] * increase_by,
                    "A",
                    last_decreased,
                    a_by,
                    b_by,
                )
            elif (
                x + increases["B"]["x"] <= prize["x"]
                and y + increases["B"]["y"] <= prize["y"]
                and b_by < 100
                and last_decreased != "B"
            ):
                # increase in B would not overshoot
                # check how many can increase?
                increase_by = how_many_increases(
                    x, y, increases["B"]["x"], increases["B"]["y"]
                )
                b_by += increase_by
                moves(
                    x + increases["B"]["x"] * increase_by,
                    y + increases["B"]["y"] * increase_by,
                    "B",
                    last_decreased,
                    a_by,
                    b_by,
                )
            else:
                # both would overshoot
                # remove by other than last increased so it doesn't go in a loop
                if last_increased == "A":
                    decrease_by = b_by - 100 if b_by > 100 else 1
                    b_by -= decrease_by
                    if b_by < 0:
                        # too much reduction, no go
                        return False
                    moves(
                        x - increases["B"]["x"] * decrease_by,
                        y - increases["B"]["y"] * decrease_by,
                        last_increased,
                        "B",
                        a_by,
                        b_by,
                    )
                else:
                    decrease_by = a_by - 100 if a_by > 100 else 1
                    a_by -= decrease_by
                    if a_by < 0:
                        # too much reduction, no go
                        return False
                    moves(
                        x - increases["A"]["x"] * decrease_by,
                        y - increases["A"]["y"] * decrease_by,
                        last_increased,
                        "A",
                        a_by,
                        b_by,
                    )

    for line in data:
        if line:
            coords = line.split(":")[-1]
            if "Button A" in line:
                coords = [int(i.split("+")[-1]) for i in coords.split(", ")]
                increases["A"]["x"] = coords[0]
                increases["A"]["y"] = coords[1]
            elif "Button B" in line:
                coords = [int(i.split("+")[-1]) for i in coords.split(", ")]
                increases["B"]["x"] = coords[0]
                increases["B"]["y"] = coords[1]
            else:
                coords = [int(i.split("=")[-1]) for i in coords.split(", ")]
                prize["x"] = coords[0]
                prize["y"] = coords[1]

                # start with A
                inc_a_x = prize["x"] // increases["A"]["x"]
                inc_a_y = prize["y"] // increases["A"]["y"]
                if inc_a_x >= 100 and inc_a_y >= 100:
                    # no chance to win
                    continue
                by = min(inc_a_x, inc_a_y)
                moves(
                    increases["A"]["x"] * by, increases["A"]["y"] * by, "A", "A", by, 0
                )

                # start with B
                inc_b_x = prize["x"] // increases["B"]["x"]
                inc_b_y = prize["y"] // increases["B"]["y"]
                if inc_b_x >= 100 and inc_b_y >= 100:
                    # no chance to win
                    continue
                by = min(inc_b_x, inc_b_y)
                moves(
                    increases["B"]["x"] * by, increases["B"]["y"] * by, "B", "B", 0, by
                )

                # reset
                increases = {"A": {"x": 0, "y": 0}, "B": {"x": 0, "y": 0}}
                inc_a_x = 0
                inc_a_y = 0
                inc_b_x = 0
                inc_b_y = 0
                by = 0
                prize = {"x": 0, "y": 0}
        if results:
            part_1_result += results
            results = 0

    pt_1_end = time()
    print("Part 1: ", part_1_result, " in ", pt_1_end - start, " seconds")

    # part 2
    pt_2_end = time()
    print("Part 2: ", part_2_result)
