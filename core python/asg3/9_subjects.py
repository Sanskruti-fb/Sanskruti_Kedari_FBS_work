# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))
mark4 = float(input("Enter marks for subject 4: "))
mark5 = float(input("Enter marks for subject 5: "))


total_marks = mark1 + mark2 + mark3 + mark4 + mark5


percentage = (total_marks / 500) * 100


if percentage >= 80 and percentage <= 100:
    print("First class with Distinction")
elif percentage >= 70 and percentage < 80:
    print("First Class")
elif percentage >= 60 and percentage < 70:
    print("Higher Second Class")
elif percentage >= 40 and percentage < 60:
    print("Second Class")
elif percentage >= 0 and percentage < 40:
    print("Fail")
else:
    print("Invalid Marks Entered.")
