lst = [1, 0, 3, 0, 0, 0, 5]
result = []
zeros = []
for n in lst:
    if n == 0:
        zeros.append(n)
    elif n != 0:
        result.append(n)
print(result + zeros)
