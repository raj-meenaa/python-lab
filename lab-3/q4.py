def calculate_price(original_price, discount_percentage=10):
    """
    This function calculates the price after applying the discount.
    
    :param original_price: The original price of the item.
    :param discount_percentage: The discount percentage to be applied (default is 10%).
    :return: The final price after applying the discount.
    """
    discount_amount = (discount_percentage / 100) * original_price
    final_price = original_price - discount_amount
    return final_price


original_price = float(input("Enter the original price: "))

custom_discount = input("Do you want to provide a custom discount percentage (yes/no)? ").lower()

if custom_discount == 'yes':
    discount_percentage = float(input("Enter the discount percentage: "))
    final_price = calculate_price(original_price, discount_percentage)
else:
    final_price = calculate_price(original_price)  

print(f"Final price after discount: {final_price:.2f}")