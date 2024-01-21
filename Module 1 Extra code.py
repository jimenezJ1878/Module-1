# Function to get user input and return it as int or float based on the input
def get_number(prompt):
    while True:
        user_input = input(prompt)
        # Check if the input is a valid float or integer
        if user_input.replace('.', '', 1).isdigit():
            if '.' in user_input:
                return float(user_input)
            else:
                return int(user_input)
        else:
            print("Invalid input. Please enter a valid number.")

# Main program to perform arithmetic operations
def main():
    while True:
        # Getting input from the user using the get_number function
        num1 = get_number("Enter first number (num1): ")
        num2 = get_number("Enter second number (num2): ")

        # Performing arithmetic operations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2

        # Displaying the results
        print(f"The addition of {num1} and {num2} is: {addition}")
        print(f"The subtraction of {num1} from {num2} is: {subtraction}")
        print(f"The multiplication of {num1} and {num2} is: {multiplication}")

        # Handling division by zero error for division
        if num2 != 0:
            division = num1 / num2
            print(f"The division of {num1} by {num2} is: {division}")
            break
        else:
            print("Error: Division by zero is not allowed. Please enter new numbers.")

# Running the main program
if __name__ == "__main__":
    main()