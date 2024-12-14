import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2:
        print("Please provide year and day number")
        sys.exit(1)
    year = args[0]
    day = args[1]
    with open(f"{year}/day{day}.py", "w") as f:
        f.write(f"from read_data import read_in_data\n\n")
        f.write(f"from time import time \n\n")
        f.write(f"if __name__ == '__main__':\n")
        f.write(f"    start = time()\n")
        f.write(f"    data = read_in_data('./data/day{day}.txt')\n")
        f.write(f"    part_1_result = 0\n")
        f.write(f"    part_2_result = 0\n")
        f.write(f"\n")
        f.write(f"    # part 1\n")
        f.write(f"\n")
        f.write(f"    pt_1_end = time()\n")
        f.write(f"    print('Part 1: ', part_1_result, ' in ', pt_1_end - start, ' seconds.')\n")
        f.write(f"\n")
        f.write(f"    # part 2\n")
        f.write(f"\n")
        f.write(f"    pt_2_end = time()\n")
        f.write(f"    print('Part 2: ', part_2_result, ' in ', pt_2_end - start, ' seconds.')\n")
        f.write(f"\n")
    with open(f"{year}/data/day{day}.txt", "w") as f:
        pass
