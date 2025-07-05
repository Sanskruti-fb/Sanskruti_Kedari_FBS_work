#  Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

amt = float(input("Enter ticket price per person: "))

# initially total fare
fair = 0

# person 1 and calculate fare
a1 = int(input("Enter age of person 1: "))
if a1 < 12:
    fair += amt - amt * 0.3
elif a1 > 59:
    fair += amt - amt * 0.5
else:
    fair += amt

# person 2 and calculate fare
a2 = int(input("Enter age of person 2: "))
if a2 < 12:
    fair += amt - amt * 0.3
elif a2 > 59:
    fair += amt - amt * 0.5
else:
    fair += amt

# person 3 and calculate fare
a3 = int(input("Enter age of person 3: "))
if a3 < 12:
    fair += amt - amt * 0.3
elif a3 > 59:
    fair += amt - amt * 0.5
else:
    fair += amt

# person 4 and calculate fare
a4 = int(input("Enter age of person 4: "))
if a4 < 12:
    fair += amt - amt * 0.3
elif a4 > 59:
    fair += amt - amt * 0.5
else:
    fair += amt

# person 5 and calculate fare
a5 = int(input("Enter age of person 5: "))
if a5 < 12:
    fair += amt - amt * 0.3
elif a5 > 59:
    fair += amt - amt * 0.5
else:
    fair += amt

# total ticket amount
print("Total ticket amount for 5 people is:", fair)
