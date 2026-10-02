def display_menu(menu):
    print("\n" + "=" * 45)
    print("          🍔 WELCOME TO QUICK BITE 🍟")
    print("=" * 45)
    print(f"{'No.':<5}{'Menu Item':<25}{'Price':>10}")
    print("-" * 45)

    for number, item in menu.items():
        print(f"{number:<5}{item['name']:<25}₱{item['price']:>8.2f}")

    print("=" * 45)
