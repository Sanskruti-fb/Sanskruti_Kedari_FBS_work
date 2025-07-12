# 11. WAP to check if given number Strong Number.
num = int(input("Enter the number:"))
temp = num
sum = 0

while(num != 0):
    a = num % 10
    num = num // 10
    fact = 1

    for i in range(1,a + 1):
        fact = fact * i
    
    sum = sum + fact

if(sum == temp):
    print("It is a strong number")

else:
    print("It is not a strong number")
