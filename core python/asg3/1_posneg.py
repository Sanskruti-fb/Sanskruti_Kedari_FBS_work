# Write a program to check if the given number is positive or negative.

number =int(input("Enter a number:"))

if(number == 0):
    print("Number is neutral")
elif(number > 0):
    print("Number is positive")
elif(number < 0):
    print("Number is negative")
else:
    print("Wrong output")