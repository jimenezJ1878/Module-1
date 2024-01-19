# Function to get user input and return it as int or float based on the input
def get_number(prompt):
    while True:
        try:
            # Get input from the user
            user_input = input(prompt)
            # Treat input as float if it contains a decimal point, else as integer
            return float(user_input) if '.' in user_input else int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Ask the user to input the first number (num1)
num1 = get_number("Enter first number (num1): ")

# Ask the user to input the second number (num2)
num2 = get_number("Enter second number (num2): ")

# Calculate the sum of num1 and num2
addition = num1 + num2

# Calculate the difference between num1 and num2
subtraction = num1 - num2

# Display the results
print("The addition of", num1, "and", num2, "is:", addition)
print("The subtraction of", num1, "from", num2, "is:", subtraction)
