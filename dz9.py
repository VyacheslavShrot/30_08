lst = [1, 2, 3, 4, 5, 6, 7, 9]
if len(lst) > 3:
    x = lst.pop(-2)
    y = lst.pop(0)
    c = lst.pop(1)
    print([y] + [c] + [x])
elif len(lst) == 3:
    x = lst.pop(0)
    y = lst.pop(1)
    c = lst.pop(0)
    print([x] + [y] + [c])
