import read_data
from hashlib import md5

if __name__ == "__main__":
    input = read_data.read_in_data("inputs/day_4.txt")[0]
    for i in range(10000000):
        m = md5()
        m.update(f"{input}{i}".encode())
        if m.hexdigest().startswith("000000"):
            print(i)
            break
