
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # converting the parameter to float using the float(param) constructor
    # then returning the result
    # the parameter d is expected to be convertable to float

    return float(d)


def percent_to_float(p):
    # converting the paramter to float using the float(param) constructor
    # then convering the result to percentage multiplier by dividing it by 100
    # then returning the result
    # the parameter p is expected to be convertable to float
    return float(p)/100

main()
