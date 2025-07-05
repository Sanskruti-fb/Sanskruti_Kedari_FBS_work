# Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 = float(input("Enter first angle of the triangle: "))
angle2 = float(input("Enter second angle of the triangle: "))
angle3 = float(input("Enter third angle of the triangle: "))

sum_of_angles = angle1 + angle2 + angle3

if sum_of_angles == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
