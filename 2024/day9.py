from read_data import read_in_data

if __name__ == '__main__':

    def append_to_result(block_id, spaces):
        for i in range(spaces):
            if len(result) < total_spaces_allowed:
                result.append(block_id)

    data = read_in_data('./data/day9.txt')[0]
    part_1_result = 0
    part_2_result = 0

    #part_1
    result = []
    left_index = 0
    right_index = len(data) - 1
    remainder = None
    spaces_filled = 0
    potential_spaces_left = sum(int(x) for i, x in enumerate(data) if i % 2 != 0)
    total_spaces_allowed = sum(int(x) for i, x in enumerate(data)) - potential_spaces_left

    def fill_spaces(spaces):
        global right_index
        global remainder
        global result
        global spaces_filled
        r_ind_int = int(data[right_index])
        if not spaces:
            return
        elif spaces_filled == potential_spaces_left:
            return
        elif remainder:
            if spaces >= remainder[1]:
                append_to_result(str(remainder[0]), remainder[1])
                spaces_filled += remainder[1]
                spaces -= remainder[1]
                remainder = None
                fill_spaces(spaces)
            else:
                append_to_result(str(remainder[0]), spaces)
                spaces_filled += spaces
                remainder = (remainder[0], remainder[1] - spaces)
                return
        elif spaces >= r_ind_int:
            append_to_result(str(right_index // 2), r_ind_int)
            spaces_filled += r_ind_int
            left_spaces = spaces - r_ind_int
            right_index -= 2
            fill_spaces(left_spaces)
        elif spaces < r_ind_int:
            append_to_result(str(right_index // 2), spaces)
            spaces_filled += spaces
            remainder = (str(right_index // 2), r_ind_int - spaces)
            right_index -= 2
            return


    while len(result) < total_spaces_allowed: #when they overlap, all required spaces have been filled
        if left_index % 2 == 0: # even means it fills out its own blocks
            append_to_result(str(left_index // 2), int(data[left_index]))
            left_index += 1
        else: # even means it has spaces to fill
            # fill with remainder or new data
            spaces_to_fill = int(data[left_index])
            fill_spaces(spaces_to_fill)
            left_index += 1

    # part 2

    pt_2_data = data.copy()


    part_1_result = sum(int(x)*i for i, x in enumerate(result))
    print('Part 1: ', part_1_result)

    # part 2
    print('Part 2: ', part_2_result)

