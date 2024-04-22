def main():
    # takes user input
    answer = input('What is the Answer to the Great Quesiton of Life, the Universe, and Everything? ')
    # gets the answer depending on the user input
    print(getAnswer(answer))

def getAnswer(input):
    # if the input value is equal to "42" OR "forty-two" OR "forty two" 
    # then return "Yes"
    # otherwise return "No"s
    if (input == '42' or input == 'forty-two' or input == 'forty two'):
        return 'Yes'
    return 'No'

# entry point of the app 
main()