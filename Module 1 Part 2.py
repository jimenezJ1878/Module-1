# Python program to multiply and divide two numbers

while True:
    # Getting input from the user
    num1 = float(input("Enter first number (num1): "))
    num2 = float(input("Enter second number (num2): "))

    # Multiplying the numbers
    multiplication = num1 * num2
    print("The multiplication of", num1, "and", num2, "is:", multiplication)

    # Dividing the numbers and handling division by zero error
    if num2 != 0:
        division = num1 / num2
        print("The division of", num1, "by", num2, "is:", division)
        break  # Exit the loop if division is successful
    else:
        print("Error: Division by zero is not allowed. Please enter new numbers.")
