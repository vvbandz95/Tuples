# 3 

def process_orders(orders):
    """
    Process a list of customer orders and print the order details.

    Args:
    orders (list of tuples): Each tuple contains (customer_name, product, quantity).
    """
    for order in orders:
        customer_name, product, quantity = order
        print(f"Customer: {customer_name}\nProduct: {product}\nQuantity: {quantity}\n")

# Sample order data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders can be added here
]

# Process and display the orders
process_orders(orders)
