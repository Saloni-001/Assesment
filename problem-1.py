class Calculator:
    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


obj = Calculator()

print("Calculator")

while True:
    print('''Please select operation which you want to perform:
    1) Addition (+)
    2) /Subtraction (-)
    3) Multiplication (*)
    4) Division (/)
    5) Exit''')

    select = int(input("Select operations from 1 to 5: "))
    if select in (1, 2, 3, 4, 5):
        if select == 5:
            break

        a = float(input("enter a: "))
        b = float(input("enter b: "))

        if select == 1:
            print(f"{a} + {b} = {obj.add(a, b)}")

        elif select == 2:
            print(f"{a} - {b} = {obj.substract(a, b)}")

        elif select == 3:
            print(f"{a} * {b} = {obj.multiply(a, b)}")

        elif select == 4:
            print(f"{a} / {b} = {obj.divide(a, b)}")

    else:
        print("Invalid input")
