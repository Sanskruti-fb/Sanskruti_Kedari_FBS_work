# 4. WAP to print factorial of a number .

n = int(input("Enter a number: "))

# Initialize factorial to 1
fact = 1

for i in range(1, n + 1):
    fact = fact * i

# Print the result
print("Factorial of number is", fact)
