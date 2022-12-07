from item import Item


class Inventory:
    def __init__(self, items=None):
        if not items:
            items = []
        else:
            self.items = items

    def get_item(self, name):
        item = (x for x in self.items if x.name == name)
        return item

    def add_item(self, name, price, discount_quantity=None, discount_price=None):
        if self.get_item(name):
            print("Item is already on the list")
            raise ValueError
        else:
            item = Item(name, price, discount_quantity, discount_price)
            self.items.append(item)

    def remove_item(self, name):
        item = self.get_item(name)
        if item is None:
            print("Item is not in Inventory")
            raise ValueError
        else:
            self.items.remove(item)
