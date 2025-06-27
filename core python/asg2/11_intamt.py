# Write a program to accept an integer amount from user and 
# tell minimum number of notes needed for representing that amount.

amount = int(input("Enter the amount:"))

#500
n500 = amount // 500
amount = amount % 500  #or r_amount = amount % 500
                       #or r_amount %= 500

#200
n200 = amount // 200
amount = amount % 200  #or r_amount = amount % 200
                       #or r_amount %= 200

#100
n100 = amount // 100
amount = amount % 100  #or r_amount = amount % 100
                       #or r_amount %= 100

#50
n50 = amount // 50
amount = amount % 50  #or r_amount = amount % 50
                      #or r_amount %= 50

#20
n20 = amount // 20
amount = amount % 20  #or r_amount = amount % 20
                      #or r_amount %= 20

#10
n10 = amount // 10
amount = amount % 10  #or r_amount = amount % 10
                      #or r_amount %= 10

print("Number of notes of 500:",n500)
print("Number of notes of 200:",n200)
print("Number of notes of 100:",n100)
print("Number of notes of 50:",n50)
print("Number of notes of 20:",n20)
print("Number of notes of 10:",n10)



