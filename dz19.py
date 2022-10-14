import random

a = random.randint(0, 30)
b = random.randint(0, 30)

list1, list2 = list(), list()

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

list3 = list(set1)

print(list1)
print(list2)
print(list3)