x = 100
digit = int(input("Type x:"))
left, right = divmod(digit, x)
print(left, right)
left, right = divmod(digit, 10)
print(left, right)

