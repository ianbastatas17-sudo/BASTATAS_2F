def get_order(menu):
    orders = []

    while True:
        try:
            item_number = int(input("\nEnter menu item number: "))

            if item_number not in menu:
                print("Invalid menu item. Please choose from the menu.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            item_name = menu[item_number]["name"]
            item_price = menu[item_number]["price"]

            order = {
                "name": item_name,
                "price": item_price,
                "quantity": quantity
            }

            orders.append(order)

            print(f"{quantity} x {item_name} added to your order.")

            another_order = input(
                "\nDo you want to order another item? (yes/no): "
            ).lower()

            if another_order == "no":
                break
            elif another_order != "yes":
                print("Invalid answer. Your order will continue.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    return orders
