# Write a program to enter P, T, R and calculate simple Interest.

p = int(input("Enter principle amount: "))
t = int(input("Enter no. of years: "))
r = float(input("Enter rate of interest: "))

interest = (p*t*r)/100

print("Simple interest: ",interest)