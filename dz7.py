lst = [1, 0, 2, 0, 3, 0, 0]
while 0 in lst:
    for n in lst:
        if n == 0:
            a = lst.remove(0)
            print(lst + [n])
            break



