#!/usr/bin/env python3

def tower_move(n, start, finish, middle):
    # print the moves
    # this is going to be a recursive function
    if n == 1:
        print("Move a disk from {} to {}".format(start, finish))
    else:
        tower_move(n-1, start, middle, finish)
        tower_move(1, start, finish, middle)
        tower_move(n-1, middle, finish, start)

def call_tower_move(n):
    tower_move(n, "a", "b", "c")

if __name__=="__main__":
#tower_move(3, "a", "b", "c")
    n = int(input("How many disks are there?"))
    call_tower_move(n)
