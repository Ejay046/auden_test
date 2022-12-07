class Basket:
    def __init__(self, items=None):
        if items is None:
            self.items = {}
        else:
            self.items = items

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def delete_item(self, item, quanitity=1):
        if item in self.items and self.items[item] >= quanitity:
            self.items[item] -= quanitity
            if self.items[item] == 0:
                del self.items[item]
        else:
            print("Not suffcient items to remove")
            raise ValueError

    def is_empty(self):
        return len(self.items) == 0

    def print_basket(self):
        if any(self.items):
            text = ""
            for item, quantity in self.items.items():
                text += f"\n{item} x {quantity} "
                if item.has_promotion():
                    text += f"({item.print_promotion()})"
        else:
            text = "The basket is currrently empty"
        return text

    def clear_basket(self):
        self.items = {}

    def checkout(self):
        total = 0
        for item, quantity in self.items.items():
            if item.has_promotion():
                total += quantity // item.discount_quantity * item.discount_price
                total += quantity % item.discount_quantity * item.unit_price
            else:
                total += quantity * item.unit_price
        self.clear_basket()
        return total
