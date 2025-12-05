file_path = "/Users/yokurang/Documents/Projects/aoc-py/day2/input1.txt"


def contains_repeated_nums(num):
    num_as_str = str(num)
    length = len(num_as_str)
    if length % 2 == 1:
        return False
    return num_as_str[: length // 2] == num_as_str[length // 2 :]


total = 0

try:
    with open(file_path, "r") as file:
        content = file.read().strip()
        ranges = content.split(",")
        for r in ranges:
            start, end = r.split("-")
            start = int(start)
            end = int(end)
            print(f"range={r}")
            print(f"start={start}, end={end}")
            for num in range(start, end + 1):
                if contains_repeated_nums(num):
                    total += num

        print(total)

except Exception as e:
    print(f"Exception: {e}")
