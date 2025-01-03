list_products= [ 
    {'name': 'shirts', 'price':15.5 , 'quantity': 20},
    {'name': 'Jeans', 'price':20.5 , 'quantity': 1},
    {'name': 'Watches', 'price':30.5 , 'quantity': 20}, 
    {'name': 'Shoes', 'price':25.5 , 'quantity': 4}
 ]
threshold = 10
for product in list_products:
    if threshold < product['quantity']:
        print("we have more than expected",product['name'])
        
print(type(list_products))
print(list_products[2]['name'])
def calculate_total_cost(products):
    total_cost = 0
    for product in products:
        product_cost = product['price'] *product['quantity']
        total_cost += product_cost
    return total_cost

def identify_low_stock_items(products, threshold):
    low_stock_items = []
    for product in products:
        if product['quantity'] < threshold:
            low_stock_items.append(product['name'])
    return low_stock_items

print("Inventory Details:")
for product in list_products:
    print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']},Value: {product['price'] * product['quantity']}")
    #print(f"Name: {product['name']}, Price:{product['price']}, Quantity: {product['quantity']}, Value: {product['price'] * product['quantity']}")
total_cost = calculate_total_cost(list_products)
print(f"Total Inventory Value: {total_cost}")

low_stock_threshold = 5
low_stock_items = identify_low_stock_items(list_products, low_stock_threshold)

if low_stock_items:
    print("Low Stock Items:")
    for item in low_stock_items:
        print(item)
else:
    print("No items are low in stock.")


    

