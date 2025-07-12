# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter ticket cost: "))

total = 0

for i in range(passengers):
    age = int(input("Enter age of passenger: "))

    if age < 12:
        fare = ticket_cost * 0.7  # 30% discount
    elif age > 59:
        fare = ticket_cost * 0.5  # 50% discount
    else:
        fare = ticket_cost        # no discount

    total = total + fare

print("Total fare =", total)
