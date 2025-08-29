# create a function calculate_discount that takes two parameters: price and discount_percent.
def calculate_discount(price, discount_percent):

    # applying the condition to input values to return the discounted price if discount_percent is 20 or more.
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# creating a variable to take user input for price and discount_percent.
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"Discount applied. Final price: {final_price:.2f}")
else:
    print(f"No discount applied. Original price: {price:.2f}")