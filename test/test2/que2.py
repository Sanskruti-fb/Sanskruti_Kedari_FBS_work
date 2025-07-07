# a prog to accept 3 dig num.if first dig is double of second dig and half of third dig then display
#  "yes,you have done it", otherwise display"please try next time"

num = int(input("Enter a 3 digit number:"))
          
a = num % 10
num = num // 10
b = num % 10
c = num // 10

print("Third digit",a)
print("Second digit",b)
print("First digit",c)


if ( c == 2*b and c == 1/2 *a):
    print("yes,you have done it")

else:
    print("please try next time")