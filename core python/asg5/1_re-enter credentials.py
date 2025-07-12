# 1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

correct_userid = "FBS"
correct_password = "fbs_11"

# Allow user 3 attempts
for attempt in range(1, 4):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_userid and password == correct_password:
        print("Login Successful!")
        break
    else:
        print("Incorrect credentials. Try again.")

# If all attempts used
else:
    print("Too many failed attempts. Access denied.")
