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
    n1 = float
    n2 = float
    op = ''
    input(f'Enter equation:{n1} {op} {n2}')
    calculator(n1,n2,op)
