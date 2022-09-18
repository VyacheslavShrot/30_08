lst = [0, 1, 2, 3, 4, 5]
for n in lst:
    a = (lst[::2])
if len(lst) != 0:
    x = lst.pop()
    summa = sum(a)
    total_result = (summa) * x
    print(total_result)
elif len(lst) == 0:
    print(0)