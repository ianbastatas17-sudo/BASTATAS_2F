def calculate_order(orders):
    subtotal = 0

    for order in orders:
        item_total = order["price"] * order["quantity"]
        subtotal += item_total

    # Realistic discount:
    # 10% discount for orders worth ₱500 or more
    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    total = subtotal - discount

    return subtotal, discount, total