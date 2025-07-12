# 4. Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

num = int(input("Enter the number:"))
temp = num
count = 0

while(num != 0):
    num = num // 10
    count += 1
num = temp
sum = 0 

while(num != 0):
    a = num % 10
    num = num // 10
    sum = sum + (a**count)
if(sum == temp):
    print("It's a armstrong number")
else:
    print("It is not a armstring")