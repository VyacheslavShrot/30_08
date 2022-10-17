def find_unique_value(lst: list) -> float:
    set_res = set(lst)
    list_res = lst

    for i in list_res:
        if list_res.count(i) == 1:
            list_res.remove(i)

    list_res = set(list_res)
    dif_set = set_res.difference(list_res)

    dif_set = list(dif_set)

    dif_set = ''.join(map(str, dif_set))
    dif_set = float(dif_set)

    return dif_set


print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3]))
print(find_unique_value([5, 5, 5, 0.5]))