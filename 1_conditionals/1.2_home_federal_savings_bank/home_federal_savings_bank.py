def main():
    # greet (take user input)
    greeting = input('Greet: ')
    # print how much mone to give depending on the greeting
    # getMoney parameter is stripped of excessive spaces and lowercased
    # print parameter is a formatted string 
    # that has interpolated value that is returned by the getMoney function 
    # and a $ sign in front of the value
    print(f'${getMoney(greeting.lower().strip())}')

def getMoney(input):
    # if the greeting is "hello" return 0
    if(input == "hello"):
        return 0
    # if the greeting starts with "h" return 20
    # not using elif because the return statement immediately stops execution of the function 
    if(input[0] == 'h'):
        return 20
    # if the greeting is not "hello" and does not start with "h" return 100
    return 100

# entry point of the app 
main()