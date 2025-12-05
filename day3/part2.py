file_path = "/Users/yokurang/Documents/Projects/aoc-py/day3/input1.txt"

total_joltage = 0

try:
    with open(file_path, "r") as file:
        for line in file:
            for i, e in enumerate(line.strip()):
                print(f"e={e}, i={i}")
except Exception as e:
    print(f"Exception: {e}")
