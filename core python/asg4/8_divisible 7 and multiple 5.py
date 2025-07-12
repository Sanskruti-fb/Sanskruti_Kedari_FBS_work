# 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

start = int(input("Enter starting number of range: "))
end = int(input("Enter ending number of range: "))

for i in range(start, end+1):

    if i % 7 == 0 and i % 5 == 0:
        
        print(i)



#start = int(input("Enter starting number of range: "))
#end = int(input("Enter ending number of range: "))

#print("\nNumbers divisible by 7:")
#for i in range(start, end+1):
#    if i % 7 == 0:
#        print(i)

#print("\nNumbers which are multiples of 3:")
#for i in range(start, end+1):
#    if i % 3 == 0:
#        print(i)
