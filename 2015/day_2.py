import read_data
from math import prod

if __name__ == "__main__":
    totes = 0
    ribbon = 0
    input = read_data.read_in_data("inputs/day_2.txt")
    for i in input:
        i = [int(x) for x in i.split("x")]
        sides = (i[0] * i[1], i[1] * i[2], i[2] * i[0])
        totes += sum([i * 2 for i in sides]) + min(sides)
        reduced = list(i)
        reduced.remove(max(i))
        ribbon += sum([i * 2 for i in reduced]) + prod(i)
    print(totes)
    print(ribbon)
