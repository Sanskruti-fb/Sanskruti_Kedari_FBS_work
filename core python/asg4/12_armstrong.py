# WAP to print Armstrong number within a given range

start = int(input("Enter starting number of range: "))
stop = int(input("Enter ending number of range: "))

for num in range(start, stop + 1):
    temp = num
    digits = 0
    count = 0

    # Count number of digits
    while temp > 0:
        count += 1
        temp //= 10

    temp = num
    sum = 0

    while temp > 0:
        a = temp % 10
        sum += a ** count
        temp //= 10

    # Check if Armstrong
    if sum == num:
        print(num)