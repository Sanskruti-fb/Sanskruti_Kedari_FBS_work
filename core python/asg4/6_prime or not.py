# 6. WAP to check if a given number is prime number or not.

num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
