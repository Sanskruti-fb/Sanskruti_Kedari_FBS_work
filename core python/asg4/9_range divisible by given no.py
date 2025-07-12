# 9. WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter starting number of range: "))
end = int(input("Enter ending number of range: "))

num = int(input("Enter the number to check divisibility: "))


for i in range(start, end+1):

    if i % num == 0:
        print(i)
