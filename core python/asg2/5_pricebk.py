# WAP to calculate selling price of book based on cost price and discount.

cost_price = float(input("Enter the cost price of the book: "))
discount = float(input("Enter discount percentage: "))

#Calculate discount amount
discount_amount = (discount / 100) * cost_price

#Calculate selling price
selling_price = cost_price - discount_amount


print("The selling price of the book is:",selling_price)
