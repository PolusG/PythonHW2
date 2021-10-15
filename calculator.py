def calculator(number1,number2,operator):
    '''this functions takes two numbers provided by the user and operates
    them depending on the operation provided by the user'''
    if operator == "+":
        return(int(number1 + number2))
    elif operator == "-":
        return(int(number1 - number2))
    elif operator == "*":
        return(int(number1 * number2))
    elif operator == "/":
        return(int(number1 / number2))
    elif operator == "//":
	if number2 == 0:
		return "can't divide by 0
	else:
        	return(int(number1 // number2))
    elif operator == "**":
        return(int(number1 ** number2))
    else:
        return False
def parse_input():
    '''this function takes the input provided by the user and parses it 
    so the system can define the variables according to what the user entered'''
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
