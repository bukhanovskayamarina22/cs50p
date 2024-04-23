def main():
    # get user input in camelCase, and strip from excessive whitespaces
    input = input("Enter something in camelCase: ").strip()
    # print the result of converting the string to snake_case
    print(convertToSnakeCase(input))

# function that converts a camel case string to a snake case string
def convertToSnakeCase(camel_string):
    # create an empty string to keep the intermediate and the final results 
    snake_string = ''
    # iterate over all the characters in the input string
    for char in camel_string:
        # check if the current character in quesiton is capitalized 
        # (is in the list of capital letters)
        if char in uppercases:
            # if so, append an underscore
            # and a correspondend lowercase letter
            # to the end of the resulting string
            # the lowercase letter would be found at the same index 
            # as the uppercase letter in teh uppercases list 
            # since both lists have the same length and ordered alphabetically
            snake_string += '_' + lowercases[uppercases.index(char)]
        else: 
            # otherwise just add the character to the end of the snake_string
            snake_string += char
    # after iterating over the whole string
    # return the new snake_string
    return snake_string

# list of all uppercase characters of English alphabet, in alphabetic order
# intentionally not using regex
uppercases = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# list of all lowercase characters of English alphabet
lowercases = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# the entry point of the app 
main()