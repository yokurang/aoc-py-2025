import numpy as np

file_path = "/Users/yokurang/Documents/Projects/aoc-py/day6/test.txt"

m = []
grand_total = 0

with open(file_path, "r") as file:
    for line in file:
        t = line.split()
        m.append(t)

    for i in range(len(m) - 1):
        m[i] = list(map(int, m[i]))

    m = np.array(m).T
    row, col = len(m), len(m[0]) - 1
    print(f"m={m}")
    # print(f"grand_total={grand_total}")
