# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

side1 = float(input("Enter first side of the triangle: "))
side2 = float(input("Enter second side of the triangle: "))
side3 = float(input("Enter third side of the triangle: "))

# Equilateral triangle
if side1 == side2 and side2 == side3:
    print("It is an Equilateral triangle.")

# Isosceles triangle
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("It is an Isosceles triangle.")

# If none of the above, it's a Scalae triangle
else:
    print("It is a Scalar triangle.")
