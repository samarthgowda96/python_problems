def move_zeroes(list):
    #use bubble sort algorithm to mutate the list in-place
    n = len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] == 0:
                list[j], list[j+1] = list[j+1], list[j]
    print(list)

x = [0,1,0,3,12]

move_zeroes(x)
