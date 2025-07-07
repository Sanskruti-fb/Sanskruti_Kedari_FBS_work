length = float(input("Enter length of wall in meters: "))
height = float(input("Enter height of wall in meters: "))
cost_per_sq_meter = float(input("Enter painting cost per sq meter: "))

# area of 4 walls
area = 4 * length * height

# total cost
total_cost = area * cost_per_sq_meter

print("Total painting cost is ₹", total_cost)
