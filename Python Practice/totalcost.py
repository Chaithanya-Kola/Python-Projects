"""Create a list of item prices.
Initialize a variable to track the total cost, starting at 0.
Use a for loop to iterate through the item prices and add each price to the total cost.
Set a discount threshold and define a discount rate.
Check if the total cost exceeds the discount threshold. If it does, apply the discount to the total cost.
Print the final total cost, showing the amount after the discount (if any)."""

list_items = [
    {'item': 'Shirt', 'price': 10},
    {'item': 'Jeans', 'price': 20},
    {'item': 'V-necks', 'price': 20},
    {'item': 'Round-necks', 'price': 10}
]

def calculate_total_cost(list_items):
    total_cost = 0
    for prod in list_items:
        quantity = get_quantity(prod['item'])
        item_cost = prod['price'] * quantity
        total_cost += item_cost
    return total_cost

def apply_discount(total_cost):
    discount_threshold = 100
    discount_rate = 0.1
    if total_cost > discount_threshold:
        total_cost -= total_cost * discount_rate
    return total_cost

def get_quantity(data):
    quantity=int(input(f"Enter quantity for {data}: "))
    return quantity

total_cost = calculate_total_cost(list_items)
final_cost = apply_discount(total_cost)
print("Total cost of shopping without discount: ",total_cost)
print("Total cost of shopping with discount:", final_cost)
print("Hurray!!! you got a discount :" , (total_cost-final_cost))

    
