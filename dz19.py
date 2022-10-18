import random

a = random.randint(0, 30)
b = random.randint(0, 30)

list1, list2 = list(), list()

list3 = list()

for n in range(0, a):
    if n % 3 == 0:
        list1.append(n)
    else:
        pass


for n in range(0, b):
    if n % 5 == 0:
        list2.append(n)
    else:
        pass


set1 = set()
set1.update(list1, list2)
list1 = set(list1)
list2 = set(list2)


for n in list1:
    if n in list2:
        if n % 5 == 0:
            list3.append(n)

for n in list2:
    if n in list1:
        if n % 3 == 0:
            list3.append(n)


print(list1)
print(list2)

list3 = set(list3)
print(list3)