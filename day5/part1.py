file_path = "/Users/yokurang/Documents/Projects/aoc-py-2025/day5/input.txt"

fresh_ranges = []
ingredient_ids = []

with open(file_path, "r") as file:
    ranges = True
    for line in file:
        if line == "\n":
            ranges = False
            continue
        if ranges:
            start, end = line.split("-")
            fresh_ranges.append((int(start.rstrip("\n")), int(end.rstrip("\n"))))
        else:
            ingredient_ids.append(int(line.strip()))

    fresh_ranges.sort()
    ingredient_ids.sort()
    total_fresh = 0

    merged = []
    for start, end in fresh_ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    i = 0  # for ingredients id
    j = 0  # for merged ranges

    while i < len(ingredient_ids) and j < len(merged):
        ingredient = ingredient_ids[i]
        start, end = merged[j]

        if ingredient < start:
            i += 1
        elif ingredient > end:
            j += 1
        else:
            total_fresh += 1
            i += 1

print(f"total_fresh={total_fresh}")
