from posix import access

file_path = "/Users/yokurang/Documents/Projects/aoc-py-2025/day4/input.txt"

board = []
accessible = 0

with open(file_path, "r") as file:
    for line in file:
        board.append(line)
    row, col = len(board), len(board[0])

    def is_accessible(r, c):
        if r >= 0 and r < row and c >= 0 and c < col:
            if board[r][c] == "@":
                return 1
        return 0

    for r in range(row):
        for c in range(col):
            if board[r][c] == "@":
                curr_accessible = 0
                curr_accessible += is_accessible(r + 1, c + 1)
                curr_accessible += is_accessible(r + 1, c - 1)
                curr_accessible += is_accessible(r + 1, c)
                curr_accessible += is_accessible(r, c + 1)
                curr_accessible += is_accessible(r, c - 1)
                curr_accessible += is_accessible(r - 1, c + 1)
                curr_accessible += is_accessible(r - 1, c - 1)
                curr_accessible += is_accessible(r - 1, c)
                print(f"curr_accessible={curr_accessible}")
                if curr_accessible < 4:
                    accessible += 1

    print(f"accessible={accessible}")
