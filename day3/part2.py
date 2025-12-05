file_path = "/Users/yokurang/Documents/Projects/aoc-py-2025/day3/input1.txt"
total_joltage = 0

with open(file_path, "r") as file:
    for line in file:
        n = len(line.strip())
        batteries = [(e, n - i) for i, e in enumerate(line.strip())]

        joltage = ""
        left = 0

        for i in range(12):
            right = n - (11 - i)
            choices = batteries[left:right]

            if not choices:
                print("ERROR: empty choices slice!", left, right, choices)
                break

            chosen_battery, new_left = max(choices)
            joltage += chosen_battery

            left = -new_left + n + 1

        total_joltage += int(joltage)
    print(total_joltage)
