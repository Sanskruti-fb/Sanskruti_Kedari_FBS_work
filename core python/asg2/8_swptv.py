# Write a program to swap two numbers using third variable.
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

temp = num1
num1 = num2
num2 = temp

print("The swaped number is-")
print("First number:",num1)
print("Second number:",num2)


