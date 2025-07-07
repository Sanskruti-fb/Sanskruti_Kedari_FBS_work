length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))
radius = float(input("Enter the radius of semicircle: "))


#area of rectangle (length × breadth)
area_rectangle = length * breadth

# area of semicircle (1/2 × π × r × r)
area_semicircle = 0.5 * 3.14 * radius * radius

#total area (rectangle + semicircle)
total_area = area_rectangle + area_semicircle

# Perimeter = 2 × (length + breadth)
# But one side of breadth is replaced by semicircle's curved part
perimeter_rectangle_part = 2 * length + 2 * breadth - 2 * radius

# Calculate perimeter of semicircle (π × r)
perimeter_semicircle = 3.14 * radius

# total perimeter (rectangle part + semicircle)
total_perimeter = perimeter_rectangle_part + perimeter_semicircle

print("Area of rectangle =", area_rectangle)
print("Area of semicircle =", area_semicircle)
print("Total Area of figure =", total_area)

print("Perimeter of rectangle part =", perimeter_rectangle_part)
print("Perimeter of semicircle =", perimeter_semicircle)
print("Total Perimeter of figure =", total_perimeter)
