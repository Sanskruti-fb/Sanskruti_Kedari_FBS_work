# given values
radius = 20
length = 50
breadth = 40
cost_per_meter = 35

# perimeter calculations
circumference = 2 * 3.14 * radius
rect_perimeter = 2 * (length + breadth)

# total fencing length for 5 rounds
total_length = 5 * (circumference + rect_perimeter)

# total cost
total_cost = total_length * cost_per_meter

print("Total cost of fencing is ₹", total_cost)

