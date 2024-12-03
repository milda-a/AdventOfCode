from read_data import read_in_data
import re

if __name__ == "__main__":
    data = read_in_data("./data/day3.txt")

    # part 1
    result = re.findall(r"(mul\(\d{1,3},\d{1,3}\))", "".join(data))
    result = [
        x.replace("mul", "").replace("(", "").replace(")", "").split(",")
        for x in result
    ]
    total = sum(int(x[0]) * int(x[1]) for x in result)
    print(total)

    # part 2
    result = re.findall("(mul\(\d{1,3},\d{1,3}\))|(don't\(\))|(do\(\))", "".join(data))
    result = ["".join(x) for x in result]
    total_part_2 = 0
    do = True
    for each in result:
        if do:
            if "don't" in each:
                do = False
                continue
            elif "mul" in each:
                each = (
                    each.replace("mul", "").replace("(", "").replace(")", "").split(",")
                )
                total_part_2 += int(each[0]) * int(each[1])
        else:
            if "do" in each and "don't" not in each:
                do = True
                continue
    print(total_part_2)
