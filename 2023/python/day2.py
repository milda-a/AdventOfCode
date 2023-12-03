from read_data import read_in_data

if __name__ == "__main__":
    input = read_in_data("../inputs/day2.txt")
    games_and_rolls = {}
    id_sum = 0  # for part one
    total_cubes_needed = 0  # for part two
    for line in input:
        split_line = line.split(";")
        game_name_and_first_roll = split_line[0].split(":")
        games_and_rolls[game_name_and_first_roll[0]] = [
            [x.strip() for x in y.split(",")]
            for y in [game_name_and_first_roll[-1].strip(), *split_line[1:]]
        ]
    # print(games_and_rolls)
    for game_name, rolls in games_and_rolls.items():
        red, green, blue = (0, 0, 0)
        for roll in rolls:
            for each_colour in roll:
                if "red" in each_colour:
                    red = max(int(each_colour.split(" ")[0]), red)
                elif "green" in each_colour:
                    green = max(int(each_colour.split(" ")[0]), green)
                else:
                    blue = max(int(each_colour.split(" ")[0]), blue)

        # part one answer
        if red <= 12 or green <= 13 or blue <= 14:
            id_sum += int(game_name.split(" ")[-1])

        # part two answer
        total_cubes_needed += red * green * blue

    print(id_sum)
    print(total_cubes_needed)
