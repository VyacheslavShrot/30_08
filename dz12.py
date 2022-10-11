import string

name = input("Введите имя: ")
name = name.title()
a = string.punctuation + " "

for n in a:
    name = name.replace(n, '')

name = f"#{name}"

if len(name) > 140:
    name = name[:140]

print(name)
