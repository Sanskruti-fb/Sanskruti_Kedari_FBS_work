# Write a program to convert days into years, weeks and days.

ndays = int(input("Enter number of days: "))

years = ndays//365
days = years%365

weeks = days//7
days = weeks%7

print("enter number of years: ",years)
print("enter number of weeks: ",weeks)
print("enter number of days: ",days)

