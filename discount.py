def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
def main():
    original_price = float(input("Enter the original price of the item:  "))
    discount_percentage = float(input("Enter the discount percentage:  "))
    final_price = calculate_discount(original_price, discount_percentage)

    if final_price == original_price:
        print(f"No discount applied: The price remains: {final_price:2f}")
    else:
        print(f"The final price after {discount_percentage}% discount is: {final_price:2f}")

if __name__ == "__main__":
    main()
    
                        