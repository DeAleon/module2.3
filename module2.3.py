my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
nember = 0
my_list.remove(0)
while nember < len(my_list):
    if my_list[nember] >= 0:
        print(my_list[nember])
        nember += 1

    else:
        break




