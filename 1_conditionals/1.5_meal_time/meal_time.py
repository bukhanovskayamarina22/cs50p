def main():
    # takes user input
    time = input('Time, in hh:mm or h:mm format: ')
    # print meal time
    # pad input with a 0 from the left, if the input it in h:mm format
    print(getMealTime(time if (len(time) == 5) else "0"+time))

def getMealTime(input):
    # split time into hours and minutes
    hours, minutes = input.split(':')
    match hours:
        # time for a meal can start with 2 possible hour values 
        case "07" | "08":
            # if the time is the second meal hour 
            # only return meal time if minutes is "00"
            if (hours == "08"):
                if (minutes == "00"):
                    return 'breakfast time' 
            else:
                return 'breakfast time'
        case "12" | "13":
            if (hours == "13"):
                if (minutes == "00"):
                    return 'lunch time' 
            else:
                return 'lunch time'
        case "18" | "19":
            if (hours == "19"):
                if (minutes == "00"):
                    return 'dinner time' 
            else:
                return 'dinner time'
        

# entry point of the app 
main()