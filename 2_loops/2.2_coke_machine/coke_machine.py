def main():
    # call the function with logic
    acceptCoinInALoop()


def acceptCoinInALoop():
    # hardcoding the price
    due = 50
    # while the user have not paid the full price
    while(due > 0):
        # print the amount due to pay
        print(f"Amount due: {due}")
        # accept a coin, strip from whitespaces, and convert to int
        coin = int(input("Insert coin: ").strip())
        # only accept coins of the denominations: 25, 10, or 5
        # (the integer coin must be equal to any of those)
        # if the coin is not one of those - ignore it
        
        if (coin != 25 and coin != 10 and coin != 5):
        # continue the loop 
        # (stop execution of the current cycle, and continue executing the loop)
            continue
        # if the coin is of allowed denomination
        else:
            # consider this amount to be paid
            # (subtract the value of coin from the due)
            due -= coin
            # continue the cycle 
            continue
    # after the loop has ended
    # (loop condition had resulted to False)
    # pring the owed change 
    # (the absolute value of the due value)
    # (which would be <= 0)    
    print(f"Change owed: {abs(due)}")    
        
# entry point of the app 
main()

# version that uses recursion 
# accidently wrote it first, because I forgot that the chapter is called "loops"
# and we are supposed to use loops
# leaving it here because I like the recursive version better
# def main():
    # acceptCoin(50)

# def acceptCoin(due):
#     coin = int(input("Insert coin: ").strip())

#     if (coin != 50 and coin != 25 and coin != 5):
#         print(f"Amount due: {due}")
#         acceptCoin(due)
#     else:
#         due -= coin
#         if (due <= 0):
#             print(f"Change owed: {abs(due)}")
#         else:
#             print(f"Amount due: {due}")
#             acceptCoin(due)