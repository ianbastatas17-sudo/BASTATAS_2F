def print_receipt(orders, subtotal, discount, total):
    print("\n")
    print("=" * 50)
    print("              QUICK BITE")
    print("           OFFICIAL RECEIPT")
    print("=" * 50)

    print(f"{'Item':<20}{'Qty':>5}{'Price':>10}{'Total':>12}")
    print("-" * 50)

    for order in orders:
        item_total = order["price"] * order["quantity"]

        print(
            f"{order['name']:<20}"
            f"{order['quantity']:>5}"
            f"₱{order['price']:>9.2f}"
            f"₱{item_total:>11.2f}"
        )

    print("-" * 50)

    print(f"{'Subtotal:':<38}₱{subtotal:>9.2f}")
    print(f"{'Discount:':<38}₱{discount:>9.2f}")
    print(f"{'TOTAL:':<38}₱{total:>9.2f}")

    print("=" * 50)
    print("       Thank you for ordering!")
    print("          Please come again!")
    print("=" * 50)
