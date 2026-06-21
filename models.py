class Item:
    def __init__(self, name, price, category, popularity_rating):
        # Creates a food item with all required details for display and ordering
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Catalog:
    def __init__(self):
        # Starts with an empty list that will hold all available food items
        self.items = []

    def add_item(self, item):
        # Registers a new Item into the catalog so customers can browse it
        self.items.append(item)

    def filter_by_category(self, category):
        # Returns only the items that belong to the requested category (e.g. "Drinks")
        return [i for i in self.items if i.category == category]


class Transaction:
    def __init__(self):
        # Starts with an empty list that will hold the items a customer selects
        self.selected_items = []

    def add_to_order(self, item):
        # Adds a chosen Item to this transaction before checkout
        self.selected_items.append(item)

    def compute_total(self):
        # Sums the price of every item in the order and returns the total cost
        return sum(item.price for item in self.selected_items)


class Customer:
    def __init__(self, name):
        # Creates a customer with a name and an empty purchase history
        self.name = name
        self.purchase_history = []

    def record_purchase(self, transaction):
        # Saves a completed Transaction to the customer's purchase history
        self.purchase_history.append(transaction)

    def is_verified(self):
        # Returns True if the customer has at least one past purchase, False otherwise
        return len(self.purchase_history) > 0


# --- Scenario ---

# Build the catalog
catalog = Catalog()
catalog.add_item(Item("Spicy Burger",   8.99, "Burgers", 4.8))
catalog.add_item(Item("Classic Burger", 7.49, "Burgers", 3.9))
catalog.add_item(Item("Large Soda",     2.49, "Drinks",  4.1))
catalog.add_item(Item("Lemonade",       3.29, "Drinks",  4.5))
catalog.add_item(Item("Chocolate Cake", 4.99, "Desserts", 4.7))
catalog.add_item(Item("Vanilla Cup",    3.99, "Desserts", 4.2))

# Filter by category
drinks = catalog.filter_by_category("Drinks")
print("Drinks menu:")
for d in drinks:
    print(f"  {d.name} - ${d.price}")

# Sort the full catalog by popularity (highest first)
sorted_catalog = sorted(catalog.items, key=lambda i: i.popularity_rating, reverse=True)
print("\nFull catalog by popularity:")
for item in sorted_catalog:
    print(f"  {item.name} ({item.popularity_rating}) - ${item.price}")

# Customer places an order
customer = Customer("Alex")
print(f"\n{customer.name} is placing an order...")
order = Transaction()
order.add_to_order(catalog.items[0])  # Spicy Burger
order.add_to_order(catalog.items[2])  # Large Soda
order.add_to_order(catalog.items[4])  # Chocolate Cake
print(f"{customer.name}'s items:")
for item in order.selected_items:
    print(f"  - {item.name}: ${item.price}")
print(f"{customer.name}'s order total: ${order.compute_total():.2f}")

# Record the purchase and verify the customer
print(f"\nIs {customer.name} verified before purchase? {customer.is_verified()}")
customer.record_purchase(order)
print(f"Is {customer.name} verified after purchase?  {customer.is_verified()}")
print(f"{customer.name} has {len(customer.purchase_history)} transaction(s) on record.")
