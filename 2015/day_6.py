import read_data

grid = [[0 for _ in range(1000)] for _ in range(1000)]
test_grid = [[0 for _ in range(3)] for _ in range(3)]


def operate_grid(instruction, x, y, grid_to_use):
    for i in range(x[0], x[1]+1):
        for j in range(y[0], y[1]+1):
            if instruction[0] == "toggle":
                grid_to_use[i][j] += 2
            elif instruction[1] == "on":
                grid_to_use[i][j] += 1
            else:
                grid_to_use[i][j] = grid_to_use[i][j] - 1 if grid_to_use[i][j] > 0 else 0


def main(input):
    instructions = [x.split() for x in input]
    for instruction in instructions:
        first_coords = instruction[-3].split(",")
        second_coords = instruction[-1].split(",")
        x_coords = (int(first_coords[0]), int(second_coords[0]))
        y_coords = (int(first_coords[1]), int(second_coords[1]))
        operate_grid(instruction[:2], x_coords, y_coords, grid)


if __name__ == '__main__':
    input = read_data.read_in_data("inputs/day_6.txt")
    # input = ["toggle 0,0 through 2,2", "turn off 0,0 through 1,1"]
    main(input)
    total = 0
    for x in grid:
        total += sum(x)
    print(total)