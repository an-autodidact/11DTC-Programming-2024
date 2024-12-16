# Write a program to read in two numbers and divide
# the second number by the first
# you should print out if the numbers are divisible 
# without a remainder

# Extension, try to use a while loop so that the program will
# repeat endlessly

numerator = input("Enter a positive number: ")

denominator = input("Enter a whole number to divide by")

numerator = int(numerator)
denominator = int(denominator)

if(0 == numerator % denominator):
    print(str(numerator) + " is divisible by" + str(denominator))
else: 
    print(str(numerator) + " is divisible by" + str(denominator))