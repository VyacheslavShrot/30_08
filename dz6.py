lst = [1, 2, 3]
if len(lst) == 0:
    print(lst)
elif len(lst) == 1:
    print(lst)
else:
    num_last = lst.pop()
    a = ([num_last] + lst)
    print(a)
