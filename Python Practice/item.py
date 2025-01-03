# String (to store item names), Float (for prices), Integer (for quantities), List, and Dictionary
shopping_cart = []  # List to hold cart items

# Function to add an item to the shopping cart
def add_item(name, price, quantity):
    item = {
        "name": name,       # String
        "price": price,     # Float
        "quantity": quantity  # Integer
    }
    shopping_cart.append(item)  # Add the dictionary to the list

# While loop for user interaction
while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Calculate Total")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")  # Get user input (String)
    
    if choice == "1":  # Add Item
        name = input("Enter the item name: ")
        price = float(input("Enter the item price: "))  # Convert input to Float
        quantity = int(input("Enter the item quantity: "))  # Convert input to Integer
        add_item(name, price, quantity)
        print(f"{quantity} {name}(s) added to your cart.")
    
    elif choice == "2":  # View Cart
        if not shopping_cart:  # Check if cart is empty
            print("Your cart is empty!")
        else:
            print("\nYour Shopping Cart:")
            for i, item in enumerate(shopping_cart):  # Loop through List
                print(f"{i + 1}. {item['name']} - ${item['price']} x {item['quantity']}")
    
    elif choice == "3":  # Calculate Total
        total_cost = sum(item['price'] * item['quantity'] for item in shopping_cart)  # Calculate total using a generator
        print(f"\nTotal cost of your cart: ${total_cost:.2f}")
    
    elif choice == "4":  # Exit
        print("Thank you for shopping! Goodbye!")
        break  # Exit the while loop
    
    else:  # Invalid input
        print("Invalid choice. Please enter a number between 1 and 4.")