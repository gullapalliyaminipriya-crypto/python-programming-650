
# Laboratory Chemical Inventory Validation

# Hypothetical maximum quantities
max_quantity = {
    "ACID": 10,
    "BASE": 8,
    "FLAMMABLE": 15,
    "GENERAL": 20
}

# Hypothetical incompatible storage categories
incompatible_pairs = [
    ("ACID", "BASE")
]

inventory = []

n = int(input("Enter number of chemical records: "))

# Read inventory records
for i in range(n):
    print(f"\nRecord {i + 1}")
    name = input("Enter chemical name: ")
    category = input("Enter storage category: ").upper()
    quantity = float(input("Enter quantity: "))
    location = input("Enter storage location: ")

    inventory.append({
        "name": name,
        "category": category,
        "quantity": quantity,
        "location": location,
        "errors": []
    })

# Validate category and quantity
for item in inventory:
    category = item["category"]

    if category not in max_quantity:
        item["errors"].append("Invalid storage category")
    elif item["quantity"] > max_quantity[category]:
        item["errors"].append("Maximum quantity exceeded")

# Check compatibility at the same location
for i in range(len(inventory)):
    for j in range(i + 1, len(inventory)):
        a = inventory[i]
        b = inventory[j]

        same_location = (
            a["location"].strip().lower()
            == b["location"].strip().lower()
        )

        pair = (a["category"], b["category"])
        reverse_pair = (b["category"], a["category"])

        if same_location and (
            pair in incompatible_pairs
            or reverse_pair in incompatible_pairs
        ):
            a["errors"].append(
                f"Incompatible with {b['name']} at same location"
            )
            b["errors"].append(
                f"Incompatible with {a['name']} at same location"
            )

# Display validation results
print("\n--- INVENTORY VALIDATION REPORT ---")

valid_count = 0
invalid_count = 0

for item in inventory:
    print(f"\nChemical: {item['name']}")
    print(f"Category: {item['category']}")
    print(f"Quantity: {item['quantity']}")
    print(f"Location: {item['location']}")

    if item["errors"]:
        print("Status: INVALID")
        for error in item["errors"]:
            print("Reason:", error)
        invalid_count += 1
    else:
        print("Status: VALID")
        valid_count += 1

print("\n--- SUMMARY ---")
print("Total records:", n)
print("Valid records:", valid_count)
print("Invalid records:", invalid_count)

