# Find the sum of three-digit number.

num = int(input("Enter a three digit number:"))

a = num % 10
num = num // 10
c = num % 10
d = num // 10
sum = a+c+d

print("Enter the sum of three digit number:",sum)