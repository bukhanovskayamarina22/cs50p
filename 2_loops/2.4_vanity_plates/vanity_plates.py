def main():
    # requesting user input, stripping from whitespace
    # converting to lowercase for convinience
    user_input = input("Plate: ").strip().lower()
    # printing the result of validation 
    print(validate_plate(user_input))

# function to validate a lincense plate
def validate_plate(input):
    # the length of the plate must be in between 2 and 6
    if(len(input) < 2 or len(input) > 6):
        return "Invalid"
    # the first 2 characters must be letters 
    if(input[0] not in letters or input[1] not in letters):
        return "Invalid"
    # iterating over the input string with access to the current index 
    # the min value is 2
    # the max value for the iteration is the string length - 1
    # because iterables in python are zero-indexed
    # so the first element is acually the zeroth and so forth
    # the default step is 1, therefore ommited
    for i in range(2, len(input)-1):
        # no periodds,spaces, or punctuation marks are allowed
        # in other words, all symbols must be either letters or numbers 
        if(input[i] not in letters or input[i] not in numbers):
            return "Invalid"
        # if the plate has any numbers
        if(input[i] in numbers):
            # the first number in number sequence cannot be 0
            # checking if the number is 0 and if the number is first number
            # (the character before is not a number)
            if(input[i] == '0' and input[i-1] not in numbers):
                return "Invalid"
            # iterating over the rest of the characters starting from the first number
            for j in range(i, len(input)-1):
                # numbers cannot be in the middle 
                # in other words, if a number is met 
                # no letters are allowed after it 
                if input[j] in letters:
                    return "Invalid"
            # breaking from the cycle since all characters
            # are already checked in the inner cycle
            break
    # if no return happened yet, then the plate is valid
    return "Valid"

# all letters in lowercase
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# all numbers 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# entry point of the app 
main()

