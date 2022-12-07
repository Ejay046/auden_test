from item import Item
from basket import Basket

# checkout item with no promotions applied
def test_checkout_no_promotions():
    item1 = Item("A", 20)
    basket = Basket()
    basket.add_item(item1, 2)
    final_price = basket.checkout()
    assert final_price == 40


# checkout item with promotion applied once
def test_checkout_with_promotion():
    item1 = Item("A", 20, 2, 30)
    basket = Basket()
    basket.add_item(item1, 2)
    final_price = basket.checkout()
    assert final_price == 30


# checkout multiple item with promotion applied multiple times
def test_checkout_with_multiple_promotions():
    item1 = Item("A", 20, 2, 30)
    item2 = Item("B", 300, 10, 250)
    basket = Basket()
    basket.add_item(item1, 4)
    basket.add_item(item2, 30)
    final_price = basket.checkout()
    assert final_price == (3 * 250 + 2 * 30)


# checkout item with promotion applied and at normal price
def test_checkout_with_multiple_promotions():
    item1 = Item("A", 20, 2, 30)
    item2 = Item("B", 300, 10, 250)
    basket = Basket()
    basket.add_item(item1, 4)
    basket.add_item(item2, 30)
    final_price = basket.checkout()
    assert final_price == (3 * 250 + 2 * 30)


# checkout item with promotion applied and at normal price
def test_checkout_with_and_without_promotions():
    item1 = Item("A", 20, 2, 30)
    basket = Basket()
    basket.add_item(item1, 5)
    final_price = basket.checkout()
    assert final_price == (2 * 30 + 20)
