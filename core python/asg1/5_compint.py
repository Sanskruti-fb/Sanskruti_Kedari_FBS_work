# Write a program to enter P, T, R and calculate Compound Interest.

p = int(input("Enter principle amount: "))
t = int(input("Enter no. of years: "))
r = float(input("Enter rate of interest: "))
n = int(input("Enter number of time interest is compounded per year: "))

a = (p*(1+r/n))**(n*t)

print("amount: ",a)

cinterest = (a-p)

print("compound interest:",cinterest)