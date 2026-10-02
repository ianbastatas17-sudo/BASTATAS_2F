class QuickBite:
    def __init__(self, menu):
        self.menu = menu
        self.orders = []
        self.subtotal = 0
        self.discount = 0
        self.total = 0

    def display_menu(self):
        print("\n" + "=" * 45)
        print("          🍔 WELCOME TO QUICK BITE 🍟")
        print("=" * 45)
        print(f"{'No.':<5}{'Menu Item':<25}{'Price':>10}")
        print("-" * 45)

        for number, item in self.menu.items():
            print(f"{number:<5}{item['name']:<25}₱{item['price']:>8.2f}")

        print("=" * 45)

    def get_order(self):
        while True:
            try:
                item_number = int(input("\nEnter menu item number: "))

                if item_number not in self.menu:
                    print("Invalid menu item. Please choose from the menu.")
                    continue

                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

                item_name = self.menu[item_number]["name"]
                item_price = self.menu[item_number]["price"]

                order = {
                    "name": item_name,
                    "price": item_price,
                    "quantity": quantity
                }

                self.orders.append(order)

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

    def calculate_order(self):
        subtotal = 0

        for order in self.orders:
            item_total = order["price"] * order["quantity"]
            subtotal += item_total

        # Realistic discount:
        # 10% discount for orders worth ₱500 or more
        if subtotal >= 500:
            discount = subtotal * 0.10
        else:
            discount = 0

        self.subtotal = subtotal
        self.discount = discount
        self.total = subtotal - discount

    def print_receipt(self):
        print("\n")
        print("=" * 50)
        print("              QUICK BITE")
        print("           OFFICIAL RECEIPT")
        print("=" * 50)

        print(f"{'Item':<20}{'Qty':>5}{'Price':>10}{'Total':>12}")
        print("-" * 50)

        for order in self.orders:
            item_total = order["price"] * order["quantity"]

            print(
                f"{order['name']:<20}"
                f"{order['quantity']:>5}"
                f"₱{order['price']:>9.2f}"
                f"₱{item_total:>11.2f}"
            )

        print("-" * 50)

        print(f"{'Subtotal:':<38}₱{self.subtotal:>9.2f}")
        print(f"{'Discount:':<38}₱{self.discount:>9.2f}")
        print(f"{'TOTAL:':<38}₱{self.total:>9.2f}")

        print("=" * 50)
        print("       Thank you for ordering!")
        print("          Please come again!")
        print("=" * 50)

    def run(self):
        self.display_menu()

        while True:
            choice = input("\nWould you like to place an order? (yes/no): ").lower()

            if choice == "yes":
                break
            elif choice == "no":
                print("\nThank you for visiting Quick Bite!")
                print("Have a great day!")
                exit()
            else:
                print("Please enter only 'yes' or 'no'.")

        self.get_order()

        if len(self.orders) == 0:
            print("\nNo items were ordered.")
            print("Thank you for visiting Quick Bite!")
        else:
            self.calculate_order()
            self.print_receipt()
