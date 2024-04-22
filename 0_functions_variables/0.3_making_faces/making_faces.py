# takes user input 
# then the "replace" method is applied 
# this method looks for ':)' and replaces all occurences with '🙂'
# then the "replace" method is applied again, this time with arguments ':(' and '🙁'
# the result is printed
print(input('your input with emoticons: ').
      replace(':)', '🙂').
      replace(':(', '🙁'))