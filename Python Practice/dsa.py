products = [
    {'name': 'Shirt', 'price': 19.99, 'quantity': 10},
    {'name': 'Jeans', 'price': 29.99, 'quantity': 5},
    {'name': 'T-Shirt', 'price': 9.99, 'quantity': 20},
    {'name': 'Shoes', 'price': 49.99, 'quantity': 3},
    {'name': 'Hat', 'price': 9.99, 'quantity': 15}
]

total_value = 0
low_stock_items = []
low_stock_threshold = 5

for product in products:
    total_value += product['price'] * product['quantity']
    if product['quantity'] < low_stock_threshold:
        low_stock_items.append(product['name'])

print("Inventory Details:")
for product in products:
    print(f"Name: {product['name']}, Price: ${product['price']:.2f}, Quantity: {product['quantity']}, Value: ${product['price'] * product['quantity']:.2f}")

print(f"\nTotal Inventory Value: ${total_value:.2f}")

if low_stock_items:
    print("\nLow Stock Items:")
    for item in low_stock_items:
        print(item)
else:
    print("\nNo items are low in stock.")