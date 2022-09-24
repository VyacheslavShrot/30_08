numbers = int(input("Введите 4-хзначное число:"))
print(numbers)
x = 100
digit = numbers
a, b = divmod(digit, x)
c, n = divmod(a, 10)
y, u = divmod(b, 10)
print(c)
print(n)
print(y)
print(u)
