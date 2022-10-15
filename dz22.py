def find_unique_value(lst: list) -> float:
    a = []
    b = set(lst)

    for n in b:
        a.append(n)

    return a








print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3]))
print(find_unique_value([5, 5, 5, 0.5]))