# curr = 50
# R150


# s = "818181911112111"
s = "234234234234278"
n = len(s)

lst = []
for i, e in enumerate(s):
    lst.append((e, len(s) - i))

print(max(lst[: n - 11]))
total_joltage = 0
joltage = ""
batteries = []
for i, e in enumerate(s.strip()):
    batteries.append((e, len(s) - i))  # so max takes the first largest element seen
print(f"batteries={batteries}")
# first one
left = 0
for i in range(12):
    choices = batteries[left : len(s) - (11 - i)]
    # print(f"choices={choices}")
    chosen_battery, new_left = max(choices)
    print(f"chosen_battery={chosen_battery}")
    left = -new_left + len(s) + 1
    print(f"left={left}, right={len(s) - (11 - i)}")
    joltage += chosen_battery
total_joltage += int(joltage)
print(f"total_joltage={total_joltage}")
