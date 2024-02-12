class ItemToPurchase:
    """
    A class to represent an item to purchase.
    
    Attributes:
    item_name (str): Name of the item.
    item_price (float): Price of the item.
    item_quantity (int): Quantity of the item.
    """

    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        """
        The constructor for ItemToPurchase class.

        Parameters:
        item_name (str): The name of the item (defaults to "none").
        item_price (float): The price of the item (defaults to 0.0).
        item_quantity (int): The quantity of the item (defaults to 0).
        """
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        """
        Method to calculate and print the total cost of the item based on its price and quantity.
        """
        total_price = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_price:.2f}")

# Main section of the script
if __name__ == "__main__":
    # List to store the items purchased
    items = []

    # Prompt the user for details of two items to purchase
    for i in range(2):
        # Item number
        print(f"Item {i+1}")
        
        # User input for item details
        item_name = input("Enter the item name:\n")
        item_price = float(input("Enter the item price:\n"))
        item_quantity = int(input("Enter the item quantity:\n"))
        
        # Create an instance of ItemToPurchase with the given details
        item = ItemToPurchase(item_name, item_price, item_quantity)
        
        # Append the item to the list of items
        items.append(item)

    # Display the total cost of the items
    print("\nTOTAL COST")
    
    # Initialize the variable to hold the total cost
    total_cost = 0
    
    # Calculate the total cost by iterating over each item and adding its cost
    for item in items:
        # Print the cost of the current item
        item.print_item_cost()
        # Accumulate the total cost
        total_cost += (item.item_price * item.item_quantity)

    # Print the final total cost
    print(f"Total: ${total_cost:.2f}")
