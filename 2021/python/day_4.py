from read_data import read_in_data


def solve():
    data = read_in_data("../inputs/day_4.txt")
    numbers = data.pop(0).split(',')
    numbers = [int(num) for num in numbers]
    data = [num.lstrip().replace('  ', ' ').split(' ') for num in data if num]
    boards = [data[i:i + 5] for i in range(0, len(data), 5)]
    boards = [[[int(num) for num in table_row] for table_row in board] for board in boards]
    # print(numbers)
    print(boards)

    # part 1

    while not found:
        for number in numbers:
            if found:
                break
            boards = [[[0 if num == number else num for num in board_line] for board_line in board] for board in boards]
            for board in boards:
                if found:
                    break
                for table in board:
                    if found:
                        break
                    if table.count(0) == 5:
                        print(f"found it w number {number}")
                        print(board)
                        print(sum(list(chain.from_iterable(board))) * number)
                        found = True

                for i in range(5):
                    count = 0
                    for table in board:
                        if count == 5:
                            print(f"found it w number {number}!")
                            print(sum(list(chain.from_iterable(board))) * number)
                            found = True
                            break
                        if table[i] == 0:
                            count += 1

    # part 2 

    for number in numbers:
        print(f"current number {number}")
        boards = [[[0 if num == number else num for num in board_line] for board_line in board] for board in boards]
        for board in boards:
            for table in board:
                if table.count(0) == 5:
                    print(f"found it w number {number}")
                    print(board)
                    print(sum(list(chain.from_iterable(board))) * number)
                    try:
                        boards.remove(board)
                    except ValueError:
                        print("Board already removed?")
            for i in range(5):
                count = 0
                for table in board:
                    if table[i] == 0:
                        count += 1
                    if count == 5:
                        print(f"found it w number {number}!")
                        print(sum(list(chain.from_iterable(board))) * number)
                        try:
                            boards.remove(board)
                        except ValueError:
                            print("Board already removed?")


solve()
