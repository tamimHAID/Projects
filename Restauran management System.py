menu = {
    "Coffee": 200,
    "Burger": 300,
    "Chicken": 500,
    "Ice cream": 150,
    "Sweets": 350
}

print(
    """
    Welcome to my Restaurant, Please order your food
    Coffee : 200,
    Burger : 300,
    Chicken : 500,
    Ice cream : 150,
    Sweets : 350
    """
)
"""
for item, price in menu.items():
    print(f"{item} : {price} BDT")
"""
total_price = 0

while True:
    item = input("\nWhat would you like to order, Sir? ").capitalize()
    if item in menu:
        total_price += menu[item]
        print(f"Added {item} to your order. Current total: {total_price} BDT.")
    else:
        print("Sorry, that item is not available.")
    
    another_order = input("Would you like to order something else? (yes/no) ").strip().lower()
    if another_order != "yes":
        break

print(f"\nYour final total is {total_price} BDT. Thank you for dining with us!")

