from menu_data import menu
from display_menu import display_menu
from get_order import get_order
from calculate_order import calculate_order
from print_receipt import print_receipt


display_menu(menu)


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


# Get customer orders
orders = get_order(menu)


if len(orders) == 0:
    print("\nNo items were ordered.")
    print("Thank you for visiting Quick Bite!")
else:
    subtotal, discount, total = calculate_order(orders)
    print_receipt(orders, subtotal, discount, total)