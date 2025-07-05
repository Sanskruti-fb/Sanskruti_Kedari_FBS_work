# Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random

userid = input("Enter UserID: ")
password = input("Enter Password: ")

if (userid == "FBS" and password == "fbs_123"):

    captcha = random.randint(1000, 9999)
    print("Your Captcha is:", captcha)

    user_captcha = int(input("Enter the same number (Captcha): "))

    if user_captcha == captcha:
        print("Login Successful!")
    else:
        print("Captcha Incorrect. Login Failed.")

else:
    print("Invalid UserID or Password.")




