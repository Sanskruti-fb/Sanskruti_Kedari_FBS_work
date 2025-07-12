# 5. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount. (Use looping to optimize
# the problem)

# Accept amount from user
amount = int(input("Enter the amount: "))

# List of available denominations in descending order
notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]

print("Minimum number of notes:")

# Loop through each note denomination
for note in notes:
    if amount >= note:
        count = amount // note   # Number of notes of this denomination
        amount = amount % note   # Update the remaining amount
        print(f"{note} : {count}")
