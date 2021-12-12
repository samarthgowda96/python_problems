from typing import final
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


def check_for_bingo(board):
    for i in range(5):
        if set(board[i]) == {False}:
            return True
        elif set(board[:, i]) == {False}:
            return True
        elif set(board.diagonal()) == {False}:
            return True
        elif set(np.fliplr(board).diagonal()) == {False}:
            return True
    return False


bingos_order = []
cancel_loop = False
for num in drawn_numbers:
    bingos_count = 0
    for i in range(len(bingo_boards)):
        if i not in bingos_order:
            bingo_boards[i][bingo_boards[i] == num] = False
            bingo_exists = check_for_bingo(bingo_boards[i])
            if bingo_exists:
                bingos_count += 1
                bingos_order.append(i)
        else:
            bingos_count += 1
    if bingos_count == len(bingo_boards):
        final_num_called = num
        cancel_loop = True

    if cancel_loop:
        break

print(bingo_boards[bingos_order[-1]].sum() * final_num_called)
