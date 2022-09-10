li = ["cow", "1", "cat", "2", "dog", "3"]
animals = []
num = []
for n in li:
    num.append(n) if n.isnumeric() else animals.append(n)
print(animals)
print(num)
print(li)






