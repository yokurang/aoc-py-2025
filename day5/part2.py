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
    total_fresh_ids = 0

    merged = []
    for start, end in fresh_ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    for start, end in merged:
        total_fresh_ids += end - start + 1
print(f"total_fresh_ids={total_fresh_ids}")
