import pytest
from basket import Basket
from item import Item


class TestBasket:
    def setup_method(self):
        self.basket = Basket()
        self.item1 = Item("pizza", 3)
        self.item2 = Item("bagels", 4, 3, 6)

    def teardown_method(self):
        del self.basket

    # test add item to basket
    def test_add_item_to_basket(self):
        self.basket.add_item(self.item1, 3)
        assert len(self.basket.items) == 1
        assert self.basket.items[self.item1] == 3

    # test adding the same item twice to basket
    def test_add_item_to_basket_twice(self):
        self.basket.add_item(self.item1, 3)
        self.basket.add_item(self.item1, 2)
        assert len(self.basket.items) == 1
        assert self.basket.items[self.item1] == 5

    # test deleting item from basket
    def test_deleting_item_from_basket(self):
        self.basket.add_item(self.item1, 3)
        self.basket.delete_item(self.item1)
        assert len(self.basket.items) == 1
        assert self.basket.items[self.item1] == 2

    # test deleting item from basket error
    def test_deleting_item_from_basket_error(self):
        self.basket.add_item(self.item1, 3)
        try:
            self.basket.delete_item(self.item1, 4)
            assert False
        except ValueError:
            assert True
        assert len(self.basket.items) == 1

    # test deleting last item of its type from basket
    def test_deleting_last_item_from_basket(self):
        self.basket.add_item(self.item1, 3)
        self.basket.delete_item(self.item1, 3)
        assert len(self.basket.items) == 0

    # test clear basket
    def test_clear_basket(self):
        self.basket.add_item(self.item1, 3)
        self.basket.add_item(self.item2, 2)
        self.basket.clear_basket()
        assert len(self.basket.items) == 0

    # test print basket
    def test_print_basket(self):
        self.basket.add_item(self.item1, 3)
        self.basket.add_item(self.item2, 2)
        printed_string = "\nItem: 'pizza' x 3 \nItem: 'bagels' x 2 (Promotion: 3 for 6)"
        assert printed_string == self.basket.print_basket()

    # test print basket empty
    def test_basket_is_empty(self):
        assert self.basket.is_empty() == True
        self.basket.add_item(self.item1, 3)
        assert self.basket.is_empty() == False
