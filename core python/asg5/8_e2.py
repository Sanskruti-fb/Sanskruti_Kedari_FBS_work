# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

sum = 0
sign = 1
power = 1
den = 1

for i in range(1, n+1):
    term = (x ** power) / den
    sum = sum + (sign * term)

    #Update for next term
    sign = -sign
    power = power + 1
    den = den + 2

print("Sum of series:", sum)