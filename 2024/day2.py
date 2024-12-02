from typing import List

from read_data import read_in_data

def is_safe(num1, num2):
    if abs(num1 - num2) <= 3 and num1 != num2:
        return True
    return False

if __name__ == '__main__':
    data = read_in_data("./data/day2.txt")
    data = [[int(x) for x in line.split(" ")]for line in data]

    # part 1
    safe_lines = 0
    for line in data:
        # if just ascending or descending
        if line == sorted(line) or line == sorted(line, reverse=True):
            safe = True
            # check if safe
            for i in range(len(line)-1):
                if not is_safe(line[i], line[i+1]):
                    safe = False
                    break
            if safe:
                safe_lines += 1

    print("safe lines for part 1: ", safe_lines)

    # part 2

    def is_inc(ar: List):
        how_many = sum(i < j for i, j in zip(ar, ar[1:]))
        if how_many == len(ar):
            return 0
        else:
            return abs(how_many - (len(ar)-1))

    def is_dec(ar: List):
        how_many = sum(i > j for i, j in zip(ar, ar[1:]))
        if how_many == len(ar):
            return 0
        else:
            return abs(how_many - len(ar)-1)

    safe_lines = 0
    for line in data:
        safe = True
        level_removed = False
        skip_next = False
        inc = is_inc(line)
        dec = is_dec(line)
        if inc <= 1 or dec <= 1:
            for i in range(len(line)-1):
                if skip_next:
                    skip_next = False
                    continue
                if not is_safe(line[i], line[i+1]):
                    if level_removed:
                        safe = False
                        break
                    else:
                        level_removed = True
                        if i+2 <= len(line)-1 and i-1 >= 0:
                            if not is_safe(line[i], line[i+2]):
                                if not is_safe(line[i-1], line[i+1]):
                                    safe = False
                                    break
                                else:
                                    pass
                            else:
                                skip_next = True
                        else:
                            if not is_safe(line[i-1], line[i+1]):
                                safe = False
                                break
                            else:
                                pass
        else:
            safe = False
        if safe:
            safe_lines += 1
    print("safe lines for part 2: ", safe_lines)