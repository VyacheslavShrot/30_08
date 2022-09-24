numbers = int(input("Введите 5-значное число:"))
print(numbers)
x = 100
digit = numbers
a, b = divmod(digit, x)
c, n = divmod(a, 10)
y, u = divmod(b, 10)
p, o = divmod(c, 10)

q = str(u)
g = str(y)
v = str(n)
h = str(o)
l = str(p)
print(q + g + v + h + l)

