from collections import defaultdict
from dataclasses import dataclass

from read_data import read_in_data


@dataclass
class Plants:
    area: int = 0
    perimeter: int = 0


if __name__ == "__main__":
    data = read_in_data("./data/day12.txt")
    part_1_result = 0
    part_2_result = 0

    # part 1
    plants = defaultdict(Plants)
    plant_collection = None

    for i, row in enumerate(data):
        for j, plant in enumerate(row):
            try:
                directions = {
                    "n": data[i - 1][j] or None,
                    "s": data[i + 1][j] if i < len(data) - 2 else None,
                    "w": row[j - 1] or None,
                    "e": row[j + i] if j < len(row) - 2 else None,
                }
            except:
                print(
                    f"trying to get {j} to {j+1} and {i} to {i+1}, len of data is {len(data)}, len of row is {len(row)}"
                )
            if plant_collection := plants.get(plant, None):
                plant_collection.area += 1
            else:
                plants[plant] = Plants(area=1)
                plant_collection = plants[plant]
            if not j:
                # edge of plot
                plant_collection.perimeter += 1
            elif directions["w"] != plant:
                plant_collection.perimeter += 1
            if j == len(row) - 1:
                plant_collection.perimeter += 1
            elif directions["e"] != plant:
                plant_collection.perimeter += 1

            if not i:
                # edge of plot
                plant_collection.perimeter += 1
            elif directions["n"] != plant:
                plant_collection.perimeter += 1
            if i == len(data) - 1:
                plant_collection.perimeter += 1
            elif directions["s"] != plant:
                plant_collection.perimeter += 1

    part_1_result = sum(plant.area * plant.perimeter for plant in plants.values())
    print("Part 1: ", part_1_result)

    # part 2
    print("Part 2: ", part_2_result)
