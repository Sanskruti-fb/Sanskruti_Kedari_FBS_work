# Leap year or Not a leap year

year = int(input("Enter the year: "))

if (year % 400 == 0):
    print("It is a Leap Year.")
elif (year % 100 == 0):
    print("It is Not a Leap Year")
elif (year % 4 == 0):
    print("It is a Leap Year")
else:
    print("It is Not a Leap Year")