lst = [1, 2, 3, 4, 5, 6]
lst1 = []
lst2 = []
if len(lst) == 0:
    print([lst] * 2)
elif len(lst) % 2 == 0 and len(lst) == 6:
    middle_of_list = len(lst) // 2
    print(middle_of_list)
    x = lst.pop()
    print(lst)
    print(x)