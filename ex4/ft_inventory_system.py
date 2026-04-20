import sys


inventory: dict[str, int] = {}

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    for arg in sys.argv[1:]:
        try:
            item, quantity_str = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter {arg}")
            continue
        try:
            quantity = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue
        if item in inventory:
            print(f"Redundant item {item} - discarding")
            continue
        inventory[item] = quantity

    print(f"Got inventory: {inventory}")

    print(f"Item list: {list(inventory.keys())}")

    total_quantity = sum(inventory.values())
    item_number = len(inventory.keys())
    print(f"Total quantity of the {item_number} items: {total_quantity}")

    if item_number > 0:
        for item, quantity in inventory.items():
            representation = quantity / total_quantity * 100
            print(f"Item {item} represents {representation:.2f}%")

        most_abundant_item = max(inventory.items(), key=lambda x: x[1])
        item, quantity = most_abundant_item
        print(f"Item most abundant: {item} with quantity {quantity}")

        least_abundant_item = min(inventory.items(), key=lambda x: x[1])
        item, quantity = least_abundant_item
        print(f"Item least abundant: {item} with quantity {quantity}")

    inventory['magic_item'] = 1
    print(f"Updated inventory: {inventory}")
