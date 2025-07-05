# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

# Check eligibility based on gender and age
if gender == "male" and age >= 21:
    print("Eligible for marriage.")
elif gender == "female" and age >= 18:
    print("Eligible for marriage.")
else:
    print("Not eligible for marriage.")
