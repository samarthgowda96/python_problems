import numpy as np

f = open("input.txt", "r")

nums = f.readlines()

drawn_numbers = [int(x) for x in nums[0].replace("\n", "").split(",")]
nums.pop(0)
nums = [x.strip("\n") for x in nums if x != "\n"]
bingo_boards = []

board = []
for i in range(len(nums)):
    board.append([int(x) for x in nums[i].split()])
    if len(board) == 5:
        board = np.array(board)
        bingo_boards.append(board)
        board = []


def check_for_bingo(board, num):
    for i in range(5):
        if set(board[i]) == {False}:
            return board.sum() * num
        elif set(board[:, i]) == {False}:
            return board.sum() * num
        elif set(board.diagonal()) == {False}:
            return board.sum() * num
        elif set(np.fliplr(board).diagonal()) == {False}:
            return board.sum() * num
    return None


for num in drawn_numbers:
    bingo = None
    for board in bingo_boards:
        board[board == num] = False
        final_value = check_for_bingo(board, num)
        if final_value:
            bingo = True
            print(final_value)
    if bingo:
        break
