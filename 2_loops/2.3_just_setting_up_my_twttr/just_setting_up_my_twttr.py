def main():
    # getting user input and stripping it from any excessive whitespace
    user_input = input("Input: ").strip()
    # printing the shortened string
    print(shrtn(user_input.lower()))

# takes user input and shortens it
# (removes all vowels from it)
def shrtn(long_string):
    # defining a variable to accumulate the result  
    # instantiating it to an empty string
    short_string = ''
    # iterating over the original string
    for char in long_string:
        # if the current character is a vowel 
        # (if the character is in the list of vowel characters)
        if (char in ['a', 'i', 'e', 'o', 'u']):
            # if yes, ignore the char 
            # and continue to the next iteration of the loop
            continue   
        # if the character is not a vowel 
        else:
            # include it into the result string
            # (append it to the short_string varaible)
            short_string += char 
    # upon leaving the loop, return the result
    return short_string
# entry point of the app 
main()