# Write a program to check if given 3 digit number is a palindrome or not.

num1 = int(input("Enter a 3-digit number: "))

# Check if it's a 3-digit number
if num1 >= 100 and num1 <= 999:
    # Copy original number to num2 using temp
    temp = num1
    num2 = temp  # Now num2 has same value as num1

    # Reverse the number 
    a = num2 % 10
    num2 = num2 // 10

    b = num2 % 10
    reverse = (a * 10) + b

    c = num2 // 10
    reverse = (reverse * 10) + c

    # Compare original number and reversed number
    if num1 == reverse:
        print("It is a Palindrome Number.")
    else:
        print("It is not a Palindrome Number.")

else:
    print("Please enter a valid 3-digit number.")
