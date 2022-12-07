from basket import Basket
from item import Item
from inventory import Inventory

basket = Basket()
item1 = Item("A", 20)
item2 = Item("B", 30)

item1.add_promotion(2, 10)

basket.add_item(item1, 4)
basket.add_item(item2, 3)


print("Welcome to the Shopping Cart App")
print("-----------------------")
print("1.View Basket")
print("2.Checkout")
print("3.Clear Basket")
print("4.Exit")
print("-----------------------")

while True:
    cmd = input("\n > ")

    # view items currently in the basket
    if cmd == "1":
        print(basket.print_basket())

    # checkout basket
    elif cmd == "2":
        print("Your Basket:")
        print(basket.print_basket())
        total_price = basket.checkout()
        print(f"Your Total: {total_price}")

    # clear basket
    elif cmd == "3":
        basket.clear_basket()
        print("Your Basket's Been Cleared")

    elif cmd == "4":
        break
    else:
        print(f"Unknown command: {cmd}")
