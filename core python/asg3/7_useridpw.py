# Write a program to check if user has entered correct userid and password.

userid = input("Enter UserID: ")
password = input("Enter Password: ")

# Check if both are correct
if userid == "FBS" and password == "fbs_123":
    print("Login Successful!")
else:
    print("Invalid UserID or Password.")