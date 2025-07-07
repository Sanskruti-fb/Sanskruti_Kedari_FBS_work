p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
p4 = float(input("Enter price of product 4: "))
p5 = float(input("Enter price of product 5: "))

# total price
total_price = p1 + p2 + p3 + p4 + p5

# GST calculation
gst = 0.18 * total_price

# final bill
final_bill = total_price + gst

print("Total bill after adding GST is ₹", final_bill)

