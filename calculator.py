def calculator(number1,number2,operator):
    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "*":
        print(number1 * number2)
    elif operator == "/":
        print(number1 / number2)
    elif operator == "//":
        print(number1 // number2)
    elif operator == "**":
        print(number1 ** number2)
    else:
        return False
def parse_input():
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    op = input("Enter the operator: ")
    calculator(n1,n2,op)