#Part 1: Write a program that calculates the total amount of a meal purchased at a restaurant. 
#The program should ask the user to enter the charge for the food and then calculate the amounts with an 
#18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.

print("Welcome to the Burger Place and Self-Service.")
# Ask the user to enter the charge for the food
food_charge_main = float(input("Please enter the charge for the food: $"))

# Calculate the tip and sales tax
tip = food_charge_main  * 0.18
sales_tax = food_charge_main  * 0.07

# Calculate the total price
total_price = food_charge_main  + tip + sales_tax

# Display the amounts
print(f"Food Charge: ${food_charge_main :.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total Price: ${total_price:.2f}")
