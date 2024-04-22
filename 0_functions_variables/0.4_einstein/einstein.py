# creating a variable to store the light speed value
LIGHT_SPEED = 300000000
# asking for user input and converting it to an integer, then assigning the value to the mass variable 
# the input is expected to be convertable to int 
mass = int(input('input mass: '))
# calcualting light_speed^2, then multipling it by the mass
# then printing the result
print("J: ", mass * LIGHT_SPEED ** 2)