def move_zeros(lst):
    temp = []
    zeros = []
    for i in range(len(lst)):
        if lst[i] !=0:
             temp.append(lst[i])
        else:
             zeros.append(lst[i])

    return temp+zeros
