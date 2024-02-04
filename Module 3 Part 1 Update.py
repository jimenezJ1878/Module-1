# Menu for Burger Palace
burger_menu = {
    "Classic Combo": 5.99,
    "Cheese Lover Combo": 6.99,
    "Veggie Delight Combo": 7.49
}

# Display the menu
print("Welcome to Burger Palace! Here are our burger combos:")
for combo, price in burger_menu.items():
    print(f"{combo}: ${price:.2f}")

# Initialize the total food charge
total_food_charge = 0

# Allow the user to make their selections
for combo in burger_menu:
    quantity = int(input(f"How many '{combo}' would you like to order? "))
    total_food_charge += quantity * burger_menu[combo]

# Calculate the tip and sales tax
tip = total_food_charge * 0.18
sales_tax = total_food_charge * 0.07

# Calculate the total price
total_price = total_food_charge + tip + sales_tax

# Display the amounts
print(f"\nFood Charge: ${total_food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total Price: ${total_price:.2f}")
