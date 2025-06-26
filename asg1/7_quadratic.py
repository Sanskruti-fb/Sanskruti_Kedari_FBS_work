# Program to Find the Roots of a Quadratic Equation

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

ans = (b*b) - (4*a*c)
ans = ans ** 0.5

root1 = (-b+ans)/(2*a)
root2 = (-b-ans)/(2*a)

print("enter value of first root: ",root1)
print("enter value of second root: ",root2)


