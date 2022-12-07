class Item:
    def __init__(self, name, unit_price, discount_quantity=None, discount_price=None):
        self.name = name
        self.unit_price = unit_price
        self.discount_quantity = discount_quantity
        self.discount_price = discount_price

    def __str__(self) -> str:
        return f"Item: '{self.name}'"

    def add_promotion(self, discount_quantity, discount_price):
        self.discount_quantity = discount_quantity
        self.discount_price = discount_price

    def remove_promotion(self):
        self.discount_quantity = None
        self.discount_price = None

    def has_promotion(self):
        if self.discount_quantity and self.discount_price:
            return True
        else:
            return False

    def print_promotion(self):
        return f"Promotion: {self.discount_quantity} for {self.discount_price}"
