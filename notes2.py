line = "234234234234278"
total_joltage = 0
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
assert 434234234278 == total_joltage
