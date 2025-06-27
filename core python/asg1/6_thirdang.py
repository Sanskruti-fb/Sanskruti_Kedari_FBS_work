# Write a Program to input two angles from user 
# and find third angle of the triangle.

ang1 = int(input("Enter the angle of side 1: "))
ang2 = int(input("Enter the angle of side 2: "))


ang3 = 180-(ang1+ang2)

print("angle 3 of triangle: ",ang3)