def main():
    # get expression
    print("Enter an arthemtic expression in format x y z where ")
    print("x and z are operands, and y is an operator ")
    print("(one of +, -, *, /)")
    expression = input('Expression: ')
    
    # print the result of calculation
    print(interpet(expression.strip()))

def interpet(input):
    # assuming the x y z format of the input, split the input by space 
    # the result is a list of 3 elements, x, y, and z 
    # that are the terms of the expression
    terms = input.split(' ')
    # assign the 1 operand to x (0th element of the terms list)
    # convert to a number
    x = int(terms[0])
    # assign the operator to y
    y = terms[1]
    # assign the 2 operand to z 
    # convert to a number
    z = int(terms[2])
    # match the operator to 4 possible values
    # return the result of correspondent calculation
    match y:
        case '+':
            return x+z
        case '-':
            return x-z
        case '*':
            return x*z
        case '/':
            return x/z

# entry point of the app 
main()