file_path = "/Users/yokurang/Documents/Projects/aoc-py/day3/input1.txt"

total_joltage = 0

try:
    with open(file_path, "r") as file:
        for line in file:
            curr = line[:2]
            print(f"curr={curr}")
            for i in range(2, len(line)):
                next_num = line[i]
                fst, snd, trd = curr, curr[0] + next_num, curr[1] + next_num
                curr = str(max(int(fst), int(snd), int(trd)))
            total_joltage += int(curr)
        print(f"Total Joltage: {total_joltage}")
except Exception as e:
    print(f"Exception: {e}")
