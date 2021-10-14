def calculator(number1,number2,operator):
    if operator == "+":
        print(int(number1 + number2))
    elif operator == "-":
        print(int(number1 - number2))
    elif operator == "*":
        print(int(number1 * number2))
    elif operator == "/":
        print(int(number1 / number2))
    elif operator == "//":
        print(int(number1 // number2))
    elif operator == "**":
        print(int(number1 ** number2))
    else:
        return False
def parse_input():
    userInput = input(f'Enter equation: ')
    if userInput.__contains__('+'):
        x = userInput.split("+")
        n1 = int(x[0])
        n2 = int(x[1])
        op = '+'
    elif userInput.__contains__('-'):
        x = userInput.split("-")
        n1 = int(x[0])
        n2 = int(x[1])
        op = '-'
    elif userInput.__contains__('*'):
        x = userInput.split("*")
        n1 = int(x[0])
        n2 = int(x[1])
        op = '*'
    elif userInput.__contains__('/'):
        x = userInput.split("/")
        n1 = int(x[0])
        n2 = int(x[1])
        op = '/'
    elif userInput.__contains__('//'):
        x = userInput.split("//")
        n1 = int(x[0])
        n2 = int(x[1])
        op = '//'
    elif userInput.__contains__('**'):
        x = userInput.split("**")
        n1 = int(x[0])
        n2 = int(x[1])
        op = '**'
    else:
        print('invalid operation.')
    calculator(n1,n2,op)
