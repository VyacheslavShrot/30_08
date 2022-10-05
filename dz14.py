print("Write number:")

n = int(input())

a = 0
b = 1
string = str(n)
do = len(string)

while a < do:

   b = b * (n % 10)
   n = int(((n - n % 10) / 10))
   a += 1

   if a == do:

       if b > 9:

           n = b
           b = 1
           a = 0

           string = str(n)
           do = len(string)

       else:

           break
print(b)