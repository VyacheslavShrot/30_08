def add_one(lst: list) -> list:
    a = ''

    for n in lst:
        a += str(n)

    a = int(a) + 1
    b = []

    for i in str(a):
        b.append(int(i))

    return b



print(add_one([1, 2, 3, 4]))
print(add_one([0]))
print(add_one([9, 9, 9, 9]))
print(add_one([1, 0]))
