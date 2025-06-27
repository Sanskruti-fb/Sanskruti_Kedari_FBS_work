# Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))

#feet to meters
fm = feet * 0.3048

#inches to meters
im = inches * 0.0254

#total distance in meters
total_meters = fm + im


#feet to centimeters
fc = feet * 30.48

#inches to centimeters
ic = inches * 2.54

#total distance in centimeters
total_centimeters = fc + ic


print("Distance in feet to meter:",fm)
print("Distance in feet to centimeter:",fc)

print("Distance in inches to meter:",im)
print("Distance in inches to centimeter:",ic)
