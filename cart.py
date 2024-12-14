shopping_cart = []  # List to store items

def add_item():  # Add an item to the cart
    name = input("Item name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    shopping_cart.append({"name": name, "price": price, "quantity": quantity})

def view_cart():  # Display cart items
    if not shopping_cart:
        print("Cart is empty!")
    else:
        for i, item in enumerate(shopping_cart):
            print(f"{i+1}. {item['name']} - ${item['price']} x {item['quantity']}")

def calculate_total():  # Calculate total cost
    total = sum(item['price'] * item['quantity'] for item in shopping_cart)
    print(f"Total: ${total:.2f}")

while True:  # Menu loop
    print("\n1. Add Item  2. View Cart  3. Total  4. Exit")
    choice = input("Choose (1-4): ")
    if choice == "1": add_item()
    elif choice == "2": view_cart()
    elif choice == "3": calculate_total()
    elif choice == "4": break
    else: print("Invalid choice!")