# inventory management prototype

# store the products and their stock quantities
inventory = {

    "A": 20,

    "B": 15,

    "C": 30,

    "D": 25,

    "E": 10

} 

# Display all product and their current stock
def show_inventory():

    print("\nCurrent Inventory")

    print("-----------------")

    for product, quantity in inventory.items():

        print(product + ":", quantity)
 

# Process customer order
def process_order():
       
        # Get the product selected by the customer
    product = input("\nEnter product (A-E): ").upper()

        # Check whether the product exists
    if product not in inventory:

        print("Product does not exist.")

        return

        # Ask for the order quantity
    try:

        quantity = int(input("Enter quantity: "))

        # Handle invalid number input
    except ValueError:

        print("Please enter a number.")

        return
       
        # Check for zero or negative quantities
    if quantity <= 0:

        print("Quantity must be greater than 0.")

        return
      
        # Check if there is enough stock
    if quantity > inventory[product]:

        print("Insufficient stock.")

        print("Available:", inventory[product])

        return
        
        # Calculate the Inventory
    inventory[product] = inventory[product] - quantity

        # Display the right result
    print("\nOrder accepted.")

    print("Product:", product)

    print("Quantity:", quantity)

    print("Remaining stock:", inventory[product])

# Start the inventory management system
print("Inventory Management System")

# Show the starting Inventory
show_inventory()

# Allow the user to process multiple orders
while True:

    process_order()

    show_inventory()

# Ask whether to process another order
    again = input("\nProcess another order? (Y/N): ").upper()

# Stop the program if the user chooses not to continue
    if again != "Y":

        break

# Display the ending message
print("\nProgram finished.")
