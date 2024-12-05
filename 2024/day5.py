from collections import defaultdict

from read_data import read_in_data


if __name__ == "__main__":
    data = read_in_data("./data/day5.txt")
    part_1_result = 0
    part_2_result = 0

    pages = defaultdict(list)
    updates = []

    # part 1
    for each_line in data:
        if "|" in each_line:
            priority_page, other_page = each_line.split("|")
            pages[int(priority_page)].append(int(other_page))
        elif each_line:
            updates.append([int(x) for x in each_line.split(",")])

    for each_update in updates:
        update_pending = each_update.copy()
        rule_adhered_to = True
        for i, x in enumerate(each_update):
            if common_elements := [y for y in each_update[:i] if y in pages[x]]:
                rule_adhered_to = False
                # reorder for part 2
                lowest_index = min(
                    [update_pending[:i].index(y) for y in common_elements]
                )
                update_pending.remove(x)
                update_pending.insert(lowest_index, x)
        if rule_adhered_to:
            part_1_result += each_update[(len(each_update) - 1) // 2]
        else:
            part_2_result += update_pending[(len(update_pending) - 1) // 2]

    print("Part 1: ", part_1_result)

    # part 2
    print("Part 2: ", part_2_result)
