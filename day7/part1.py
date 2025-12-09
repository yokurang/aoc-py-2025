file_path = "/Users/yokurang/Documents/Projects/aoc-py-2025/day7/input.txt"
START = "S"
SPLITTER = "^"
board = []
splits = 0

with open(file_path, "r") as file:
    for line in file:
        board.append(line.strip())

    rows, cols = len(board) - 1, len(board[0])
    beam_cols = set()
    beam_cols.add(board[0].find(START))
    for r in range(1, rows + 1):
        for c in list(beam_cols):
            if board[r][c] == SPLITTER:
                beam_cols.remove(c)
                beam_cols.add(c + 1)
                beam_cols.add(c - 1)
                splits += 1
            print(f"r={r}, beam_cols={beam_cols}, splits={splits}")
