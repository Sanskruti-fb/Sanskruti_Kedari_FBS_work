p = int(input("Enter principle amount: "))
years = int(input("Enter no. of years: "))
rate = float(input("Enter rate of interest: "))

interest = (p*years*rate)/100

print("Simple interest: ",interest)