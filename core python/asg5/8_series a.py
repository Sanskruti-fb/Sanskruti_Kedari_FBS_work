# 8. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms


n = int(input("Enter value of n: "))
sum = 0

for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact = fact * j
    sum = sum + fact

print("Sum of factorial series:", sum)
