file_path = "/Users/yokurang/Documents/Projects/aoc-py-2025/day4/input.txt"

board = []
with open(file_path, "r") as file:
    for line in file:
        line = line.rstrip("\n")
        if line:
            board.append(list(line))

row, col = len(board), len(board[0])


def is_accessible(r: int, c: int) -> bool:
    if 0 <= r < row and 0 <= c < col:
        return board[r][c] == "@"
    return False


total_accessible = 0


while True:
    to_remove = set()

    for r in range(row):
        for c in range(col):
            if board[r][c] == "@":
                accessible = 0

                neighbors = [
                    (r, c + 1),
                    (r, c - 1),
                    (r + 1, c + 1),
                    (r + 1, c - 1),
                    (r + 1, c),
                    (r - 1, c + 1),
                    (r - 1, c - 1),
                    (r - 1, c),
                ]

                for nr, nc in neighbors:
                    if is_accessible(nr, nc):
                        accessible += 1

                if accessible < 4:
                    to_remove.add((r, c))

    if not to_remove:
        break

    total_accessible += len(to_remove)

    for rr, cc in to_remove:
        board[rr][cc] = "."
print(f"total_accessible={total_accessible}")
