# List of items with their prices
shopping_list = [
    {"item": "Apple", "price": 0.5, "quantity": 4},
    {"item": "Bread", "price": 2.0, "quantity": 1},
    {"item": "Milk", "price": 1.5, "quantity": 2},
    {"item": "Eggs", "price": 0.2, "quantity": 12}
]

# Function to calculate the total cost
def calculate_total_cost(items):
    total_cost = 0  # Initialize the total cost
    for item in items:  # Loop through each item in the list
        item_cost = item["price"] * item["quantity"]  # Calculate the cost for each item
        total_cost += item_cost  # Add to the total cost
    return total_cost

# Function to print items over a specific price threshold
def print_expensive_items(items, price_threshold):
    print(f"Items costing more than ${price_threshold}:")
    for item in items:  # Loop through each item in the list
        if item["price"] > price_threshold:  # Conditional logic
            print(f"{item['item']} - ${item['price']} each")

if __name__ == "__main__":
    total = calculate_total_cost(shopping_list)  # Call the function
    print("Total cost of shopping:",total)  

    print_expensive_items(shopping_list, 1.0)
    print("print something")