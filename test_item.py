from item import Item

# test creating item without promotion
def test_create_item_without_promotion():
    item = Item("pizza", 2)
    assert item.name == "pizza"
    assert item.unit_price == 2
    assert item.discount_price == None
    assert item.discount_quantity == None


# test creating item with promotion
def test_create_item_with_promotion():
    item = Item("pizza", 2, 3, 4)
    assert item.name == "pizza"
    assert item.unit_price == 2
    assert item.discount_price == 4
    assert item.discount_quantity == 3


# test adding promotion to item
def test_add_promotion():
    item = Item("pizza", 2)
    assert item.discount_price == None
    assert item.discount_quantity == None
    item.add_promotion(3, 4)
    assert item.discount_price == 4
    assert item.discount_quantity == 3


# test removing promotion to item
def test_removing_promotion():
    item = Item("pizza", 2, 3, 4)
    assert item.discount_price == 4
    assert item.discount_quantity == 3
    item.remove_promotion()
    assert item.discount_price == None
    assert item.discount_quantity == None


# test has promotion
def test_has_promotion():
    item1 = Item("pizza", 2)
    assert item1.has_promotion() == False
    item2 = Item("bagels", 2, 3, 4)
    assert item2.has_promotion() == True


# test print promotion
def test_print_promotion():
    item = Item("bagels", 2, 3, 4)
    assert (
        item.print_promotion()
        == f"Promotion: {item.discount_quantity} for {item.discount_price}"
    )
