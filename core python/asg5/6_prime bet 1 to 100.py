# 6. Write a program to print prime numbers between 1 to 100.

print("Prime numbers between 1 to 100:")


for num in range(2, 101):

    for i in range(2, num):
        if num % i == 0:
            break  # Not prime, exit inner loop

    else:
        # Else runs only if inner loop completes without break
        print(num)


        # print(num, end=" ")       to print on same line
