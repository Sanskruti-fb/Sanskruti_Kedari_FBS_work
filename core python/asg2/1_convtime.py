# Convert the time entered in hh,min and sec into seconds.

hours = int(input("Enter hours: "))

minutes = int(input("Enter minutes: "))

seconds = int(input("Enter seconds: "))

hours_in_seconds = hours * 3600
minutes_in_seconds = minutes * 60
total_seconds = hours_in_seconds + minutes_in_seconds + seconds

print("Total time in seconds: ", total_seconds)




