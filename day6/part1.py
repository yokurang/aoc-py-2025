file_path = "/Users/yokurang/Documents/Projects/aoc-py/day6/input.txt"

m = []
grand_total = 0

with open(file_path, "r") as file:
    for line in file:
        t = line.split()
        m.append(t)

    for i in range(len(m) - 1):
        m[i] = list(map(int, m[i]))

    row, col = len(m) - 1, len(m[0])
    for c in range(col):
        if m[-1][c] == "*":
            total = 1
        else:
            total = 0
        for r in range(row):
            if m[-1][c] == "*":
                total *= m[r][c]
            elif m[-1][c] == "+":
                total += m[r][c]
        # print(f"total={total}")
        grand_total += total
    print(f"m={m}")
    # print(f"grand_total={grand_total}")
