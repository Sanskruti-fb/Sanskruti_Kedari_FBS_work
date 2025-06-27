# WAP to calculate total salary of employee based on basic, 
# da=10% of basic,ta=12% of basic, hra=15% of basic.

#da (Dearness Allowance) = 10% of basic salary
#ta (Travel Allowance) = 12% of basic salary
#hra (House Rent Allowance) = 15% of basic salary
#Total Salary = Basic + DA + TA + HRA

basic_salary = float(input("Enter the basic salary of the employee: "))

#Calculate da
da = (10 / 100) * basic_salary

#Calculate ta
ta = (12 / 100) * basic_salary

#Calculate hra
hra = (15 / 100) * basic_salary

#Calculate total salary
total_salary = basic_salary + da + ta + hra

print("Total salary of the employee is:", total_salary)

