while True:
    s = input("Знак (+, -, *, /):")
    a = float(input("a = "))
    b = float(input("b = "))
    system_con = input("Хотите дальше вычислять?")
    if system_con == "yes":
        continue
    else:
        break

    if s == "+":
        print(a + b)
    elif s == "-":
        print(a - b)
    elif s == "*":
        print(a * b)
    elif s == "/":
        if b != 0:
            print(a / b)
        else:
            print("Error")



