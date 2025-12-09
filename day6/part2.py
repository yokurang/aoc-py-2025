import collections


def part2(inputs):
    # Determine separator columns (True = separator)
    sep = [True] * (len(inputs[0]) + 5)
    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            if inputs[i][j] != " ":
                sep[j] = False

    # Parse operators from the last row
    ops = collections.deque(x for x in inputs[-1].split(" ") if x != "")

    # Set initial operator and accumulator
    p = ops.popleft()
    if p == "*":
        currentop = "*"
        current = 1
    else:
        currentop = "+"
        current = 0

    # Max width across rows
    mx = max(len(line) for line in inputs)

    ans = []

    for i in range(mx):
        if sep[i]:
            # end of a problem → store result
            ans.append(current)

            # start new problem
            p = ops.popleft()
            if p == "*":
                currentop = "*"
                current = 1
            else:
                currentop = "+"
                current = 0

            continue

        # Build number from column i
        c = 0
        for j in range(len(inputs) - 1):  # skip operator row
            if i >= len(inputs[j]):
                p = " "
            else:
                p = inputs[j][i]

            if not p.isdigit():
                continue

            c = c * 10 + int(p)

        # Apply operator
        if currentop == "+":
            current += c
        else:
            current *= c

    ans.append(current)

    print(ans)
    print(sum(ans))


# ------------------------
# LOAD FROM FILE PATH
# ------------------------


def run_from_file(file_path):
    with open(file_path, "r") as f:
        # VERY IMPORTANT: strip newline ONLY, preserve spaces
        inputs = [line.rstrip("\n") for line in f.readlines()]

    part2(inputs)


# Example usage:
run_from_file("/Users/yokurang/Documents/Projects/aoc-py-2025/day6/input.txt")
