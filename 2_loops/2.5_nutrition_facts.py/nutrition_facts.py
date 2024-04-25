def main():
    # get user input, strip from whitespace, convert to lowercase
    user_input = input("Fruit: ").strip().lower()
    # get nutrition value
    result = get_nutrition_value(user_input)
    # print result
    # if the result in None - ignore
    # end character is set to an empty string insead of the default \n
    # so that there will be no empty line in the output if the prompt is ignored
    # the result is formatted with a linebreak (\n) at the end
    # so that the terminal prompt will appear on the next line
    print(f'{result}\n' if result else '', end='')

# function go get the nutrition value of a fruit


def get_nutrition_value(input):
    # return the value by the key
    # if the key is not in the dict
    # return None
    return values.get(input)


# a dict for all the fruits
values = {'apple': 130, 'avocado': 50, 'banana': 110, 'cantaloupe': 50, 'grapefruit': 60, 'grapes': 90, 'honeydew': 50, 'kiwifruit': 90, 'lemon': 15, 'nectarine': 60,
          'orange': 80, 'peach': 60, 'pear': 100, 'pineapple': 50, 'plums': 70, 'strawberries': 100, 'sweet cherries': 100, 'tangerine': 50, 'watermelon': 80}
# entry point of the app
main()
