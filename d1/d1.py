file_path = "/Users/yokurang/Documents/Projects/aoc-py/d1/input.txt"

try:
    with open(file_path, "r") as file:
        zero_count = 0
        curr_dial = 50
        MOD = 100
        for line in file:
            print(f"Line: {line}")
            direction: str = line[0]
            if direction == "R":
                curr_dial = (curr_dial + int(line[1:])) % MOD
            elif direction == "L":
                curr_dial = ((curr_dial + MOD) - int(line[1:])) % MOD
            if curr_dial == 0:
                zero_count += 1
            print(f"curr_dial:{curr_dial}")
        print(zero_count)
except Exception as e:
    print(f"Error: {e}")
