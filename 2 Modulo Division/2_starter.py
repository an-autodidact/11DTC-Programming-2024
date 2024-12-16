num1 = 7
num2 = 5

# set count to 0 for the loop
count = 0
# iterate through the loop while count is less than 10
while(count < 10):
    # These lines are indented as they are run while the loop is true
    # check if the count is divisible by 3 (e.g. no remainder)
    if(count % 3 == 0):
        # if divisible 
        print(str(count) + " is Divisible by three")
    #  add one to count, overwrites the value in count
    count = count + 1