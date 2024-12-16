print("Hello World")

first_name = input("What is your name? ")

print("Hi " + first_name + "!")

age = input("What is your age? ")
age = int(age)

if(age >= 18):
    print("You are really old")

if first_name == "Aman":
    print("You are the best!")

print("End of the program")

count = 2
while(True):
    count = count * count
    print(count)