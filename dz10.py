import keyword
import string

name = input("Введите имя:")
a = string.punctuation.replace("_", " ")
res = True

for n in a:
    if n in name:
        res = False

if name in keyword.kwlist:
    res = False

if name != "_":
    if not name.islower():
        res = False

if name[0].isdigit():
    res = False

print(res)


