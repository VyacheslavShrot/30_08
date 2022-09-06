number1 = float(input("Type first number:"))
oper = input("Type operation:")
number2 = float(input("Type second number:"))
if oper == "+":
    print(number1 + number2)
elif oper == "-":
    print(number1 - number2)
elif oper == "*":
    print(number1 * number2)
elif oper == "/":
    print(number1 / number2)
else:
    print("Error")
