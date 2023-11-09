lst = [0, 1, 0, 12, 3]
lst_2 = [0]
non_zero = []
zero = []

for i in lst and lst_2:
    if i != 0:
        non_zero.append(i)
    else:
        zero.append(0)
result = non_zero + zero

print(result)











