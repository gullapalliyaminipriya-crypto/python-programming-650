
# Integrated E-Commerce Order Processing and Reconciliation

products = {}
orders = []
total_revenue = 0.0

# Enter product details
n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nProduct {i + 1}")
    name = input("Enter product name: ").strip()
    price = float(input("Enter unit price: "))
    stock = int(input("Enter initial stock: "))

    if not name or price < 0 or stock < 0 or name in products:
        print("Invalid or duplicate product. Skipping.")
        continue

    products[name] = {
        "price": price,
        "initial_stock": stock,
        "stock": stock,
        "actual_stock": None
    }

# Process orders
m = int(input("\nEnter number of orders: "))

for i in range(m):
    print(f"\nOrder {i + 1}")
    name = input("Enter product name: ").strip()
    quantity = int(input("Enter order quantity: "))
    discount = float(input("Enter discount percentage: "))

    if name not in products:
        print("Product not found. Order rejected.")
        continue

    if quantity <= 0 or not 0 <= discount <= 100:
        print("Invalid quantity or discount. Order rejected.")
        continue

    product = products[name]

    if quantity > product["stock"]:
        print("Insufficient stock. Order rejected.")
        continue

    # Calculate order value after discount
    price = product["price"]
    gross = price * quantity
    discount_amount = gross * discount / 100
    net_amount = gross - discount_amount

    # Dispatch products
    product["stock"] -= quantity

    returned = int(input("Enter returned quantity: "))

    if returned < 0 or returned > quantity:
        print("Invalid return quantity. Return set to zero.")
        returned = 0

    # Calculate refund using discounted unit price
    refund = (net_amount / quantity) * returned

    # Add returned products back to inventory
    product["stock"] += returned

    # Revenue after returns
    revenue = net_amount - refund
    total_revenue += revenue

    orders.append({
        "product": name,
        "quantity": quantity,
        "gross": gross,
        "discount": discount_amount,
        "refund": refund,
        "revenue": revenue
    })

    print(f"Gross amount: Rs. {gross:.2f}")
    print(f"Discount: Rs. {discount_amount:.2f}")
    print(f"Refund: Rs. {refund:.2f}")
    print(f"Revenue from order: Rs. {revenue:.2f}")

# Inventory reconciliation
print("\n--- Inventory Reconciliation ---")

for name, product in products.items():
    actual = int(input(f"Enter actual stock for {name}: "))
    product["actual_stock"] = actual

    expected = product["stock"]
    difference = actual - expected

    print(f"\nProduct: {name}")
    print(f"Initial stock: {product['initial_stock']}")
    print(f"Expected stock: {expected}")
    print(f"Actual stock: {actual}")

    if difference == 0:
        print("Status: No discrepancy")
    elif difference < 0:
        print(f"Status: Shortage of {-difference} units")
    else:
        print(f"Status: Surplus of {difference} units")

# Final order and revenue summary
print("\n--- Final Order Summary ---")
for order in orders:
    print(
        f"{order['product']}: "
        f"Quantity={order['quantity']}, "
        f"Revenue=Rs. {order['revenue']:.2f}"
    )

print(f"\nTotal revenue after returns: Rs. {total_revenue:.2f}")

print("\n--- Final Inventory Summary ---")
for name, product in products.items():
    print(f"{name}: {product['stock']} units in expected stock")

print("Reconciliation completed.")

