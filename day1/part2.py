file_path = "/Users/yokurang/Documents/Projects/aoc-py/day1/input.txt"

try:
    with open(file_path, "r") as file:
        curr_dial = 50
        MOD = 100
        zero_count = 0
        for line in file:
            print(f"line={line}")
            direction = line[0]
            clicks = int(line[1:])
            if direction == "R":
                if curr_dial == 0:
                    zero_count += clicks // MOD
                else:
                    distance_to_zero = MOD - curr_dial
                    if clicks >= distance_to_zero:
                        zero_count = zero_count + 1 + (clicks - distance_to_zero) // MOD
                curr_dial = (curr_dial + clicks) % MOD

            elif direction == "L":
                if curr_dial == 0:
                    zero_count += clicks // MOD
                else:
                    distance_to_zero = curr_dial
                    if clicks >= distance_to_zero:
                        zero_count = zero_count + 1 + (clicks - distance_to_zero) // MOD
                curr_dial = (curr_dial - clicks) % MOD
            print(f"curr_dial={curr_dial}")
            print(f"zero_count={zero_count}")
        print(f"ans={zero_count}")
except Exception as e:
    print(f"Error: {e}")
