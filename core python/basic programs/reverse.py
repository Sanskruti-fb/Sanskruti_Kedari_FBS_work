#to find the reverse of a 2 digit number

num = int(input("Enter a two digit number: "))

a = num // 10
b = num % 10
reverse = b*10+a

print("enter digit 1: ",a)
print("enter digit 2: ",b)
print("enter the reverse of the given digit: ",reverse)