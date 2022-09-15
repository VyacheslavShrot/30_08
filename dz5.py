lst = [1, 2, 3, 4, 5]
if len(lst) == 0:
    print([lst] * 2)
elif len(lst) % 2 == 0:
    middle_of_list = len(lst) // 2
    print([lst[:middle_of_list]] + [lst[middle_of_list:]])
elif len(lst) % 2 != 0:
    middle_of_list = (len(lst) // 2) + 1
    print([lst[:middle_of_list]] + [lst[middle_of_list:]])
