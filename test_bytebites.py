import unittest
from models import Item, Catalog, Transaction, Customer


# --- Item tests ---

class TestItem(unittest.TestCase):

    def test_item_stores_name(self):
        item = Item("Spicy Burger", 8.99, "Burgers", 4.8)
        self.assertEqual(item.name, "Spicy Burger")

    def test_item_stores_price(self):
        item = Item("Large Soda", 2.49, "Drinks", 4.1)
        self.assertEqual(item.price, 2.49)

    def test_item_stores_category(self):
        item = Item("Chocolate Cake", 4.99, "Desserts", 4.7)
        self.assertEqual(item.category, "Desserts")

    def test_item_stores_popularity_rating(self):
        item = Item("Lemonade", 3.29, "Drinks", 4.5)
        self.assertEqual(item.popularity_rating, 4.5)


# --- Catalog tests ---

class TestCatalog(unittest.TestCase):

    def test_catalog_starts_empty(self):
        catalog = Catalog()
        self.assertEqual(len(catalog.items), 0)

    def test_add_item_increases_catalog_size(self):
        catalog = Catalog()
        catalog.add_item(Item("Large Soda", 2.49, "Drinks", 4.1))
        self.assertEqual(len(catalog.items), 1)

    def test_add_multiple_items(self):
        catalog = Catalog()
        catalog.add_item(Item("Large Soda", 2.49, "Drinks", 4.1))
        catalog.add_item(Item("Lemonade", 3.29, "Drinks", 4.5))
        self.assertEqual(len(catalog.items), 2)

    def test_filter_by_category_returns_matching_items(self):
        catalog = Catalog()
        catalog.add_item(Item("Large Soda", 2.49, "Drinks", 4.1))
        catalog.add_item(Item("Spicy Burger", 8.99, "Burgers", 4.8))
        result = catalog.filter_by_category("Drinks")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Large Soda")

    def test_filter_by_category_returns_all_matches(self):
        catalog = Catalog()
        catalog.add_item(Item("Large Soda", 2.49, "Drinks", 4.1))
        catalog.add_item(Item("Lemonade", 3.29, "Drinks", 4.5))
        catalog.add_item(Item("Spicy Burger", 8.99, "Burgers", 4.8))
        result = catalog.filter_by_category("Drinks")
        self.assertEqual(len(result), 2)

    def test_filter_by_category_returns_empty_for_no_match(self):
        catalog = Catalog()
        catalog.add_item(Item("Spicy Burger", 8.99, "Burgers", 4.8))
        result = catalog.filter_by_category("Desserts")
        self.assertEqual(result, [])

    def test_filter_by_category_returns_empty_on_empty_catalog(self):
        catalog = Catalog()
        result = catalog.filter_by_category("Drinks")
        self.assertEqual(result, [])

    def test_filter_by_category_excludes_other_categories(self):
        catalog = Catalog()
        catalog.add_item(Item("Large Soda", 2.49, "Drinks", 4.1))
        catalog.add_item(Item("Spicy Burger", 8.99, "Burgers", 4.8))
        result = catalog.filter_by_category("Drinks")
        names = [i.name for i in result]
        self.assertNotIn("Spicy Burger", names)

    def test_filter_by_category_is_case_sensitive(self):
        catalog = Catalog()
        catalog.add_item(Item("Large Soda", 2.49, "Drinks", 4.1))
        result = catalog.filter_by_category("drinks")
        self.assertEqual(result, [])


# --- Transaction tests ---

class TestTransaction(unittest.TestCase):

    def test_transaction_starts_with_no_items(self):
        order = Transaction()
        self.assertEqual(len(order.selected_items), 0)

    def test_compute_total_is_zero_for_empty_order(self):
        order = Transaction()
        self.assertEqual(order.compute_total(), 0)

    def test_add_to_order_adds_item(self):
        order = Transaction()
        order.add_to_order(Item("Vanilla Cup", 3.99, "Desserts", 4.2))
        self.assertEqual(len(order.selected_items), 1)

    def test_compute_total_for_single_item(self):
        order = Transaction()
        order.add_to_order(Item("Large Soda", 2.49, "Drinks", 4.1))
        self.assertAlmostEqual(order.compute_total(), 2.49)

    def test_compute_total_for_multiple_items(self):
        order = Transaction()
        order.add_to_order(Item("Spicy Burger", 8.99, "Burgers", 4.8))
        order.add_to_order(Item("Large Soda", 2.49, "Drinks", 4.1))
        order.add_to_order(Item("Chocolate Cake", 4.99, "Desserts", 4.7))
        self.assertAlmostEqual(order.compute_total(), 16.47)

    def test_add_to_order_allows_duplicate_items(self):
        item = Item("Large Soda", 2.49, "Drinks", 4.1)
        order = Transaction()
        order.add_to_order(item)
        order.add_to_order(item)
        self.assertEqual(len(order.selected_items), 2)
        self.assertAlmostEqual(order.compute_total(), 4.98)


# --- Customer tests ---

class TestCustomer(unittest.TestCase):

    def test_customer_stores_name(self):
        customer = Customer("Alex")
        self.assertEqual(customer.name, "Alex")

    def test_customer_starts_with_empty_purchase_history(self):
        customer = Customer("Jordan")
        self.assertEqual(len(customer.purchase_history), 0)

    def test_is_verified_false_for_new_customer(self):
        customer = Customer("Morgan")
        self.assertFalse(customer.is_verified())

    def test_record_purchase_adds_to_history(self):
        customer = Customer("Taylor")
        customer.record_purchase(Transaction())
        self.assertEqual(len(customer.purchase_history), 1)

    def test_record_purchase_stores_correct_transaction(self):
        customer = Customer("Dana")
        order = Transaction()
        customer.record_purchase(order)
        self.assertIs(customer.purchase_history[0], order)

    def test_is_verified_true_after_purchase(self):
        customer = Customer("Casey")
        customer.record_purchase(Transaction())
        self.assertTrue(customer.is_verified())

    def test_record_multiple_purchases(self):
        customer = Customer("Riley")
        customer.record_purchase(Transaction())
        customer.record_purchase(Transaction())
        self.assertEqual(len(customer.purchase_history), 2)

    def test_is_verified_stays_true_after_multiple_purchases(self):
        customer = Customer("Sam")
        customer.record_purchase(Transaction())
        customer.record_purchase(Transaction())
        self.assertTrue(customer.is_verified())


if __name__ == "__main__":
    unittest.main()