# Sample inventory with product: quantity
inventory = {
    "Biscuits": 20,
    "Chips": 8,
    "Juice": 5,
    "Water": 50,
    "Chocolate": 3
}

LOW_STOCK_LEVEL = 10   # anything below this is considered low stock


def display_inventory():
    if not inventory:
        print("\nNo inventory available.")
        return

    print("\n--- Inventory List ---")
    for i, (item, qty) in enumerate(inventory.items(), start=1):
        print(f"{i}. {item} : {qty} units")
    print("----------------------")


def check_stock():
    print("\n--- Check Stock ---")
    item = input("Enter product name: ")

    if item not in inventory:
        print("Item not found in inventory.")
        return

    missing_amount = int(input("Enter missing amount: "))

    # Auto-assign stock levels (Flowchart logic)
    inventory[item] += missing_amount
    print(f"Stock updated! New quantity of {item}: {inventory[item]} units.")


def low_stock_process():
    print("\n--- Low Stock Items ---")
    low_list = [item for item, qty in inventory.items() if qty < LOW_STOCK_LEVEL]

    if not low_list:
        print("No low stock items.")
        return

    for item in low_list:
        print(f"{item} : {inventory[item]} units")

    # Ask if user wants to restock
    choice = input("\nWould you like to restock items? (yes/no): ")

    if choice.lower() == "yes":
        restock_item = input("Enter item to restock: ")

        if restock_item not in inventory:
            print("Item not found.")
            return

        qty = int(input("Enter quantity to add: "))
        inventory[restock_item] += qty
        print(f"Updated stock of {restock_item}: {inventory[restock_item]} units.")
    else:
        print("Returning to menu...")


def main():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Check Inventory List")
        print("2. Check Stock")
        print("3. Low Stock")
        print("4. End")

        choice = input("Select any option: ")

        if choice == "1":
            display_inventory()

        elif choice == "2":
            check_stock()

        elif choice == "3":
            low_stock_process()

        elif choice == "4":
            print("Exiting system... Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# Run program
main()