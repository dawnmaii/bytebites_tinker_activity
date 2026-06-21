class Item:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        return [i for i in self.items if i.category == category]


class Transaction:
    def __init__(self):
        self.selected_items = []

    def add_to_order(self, item):
        self.selected_items.append(item)

    def compute_total(self):
        return sum(item.price for item in self.selected_items)


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def record_purchase(self, transaction):
        self.purchase_history.append(transaction)

    def is_verified(self):
        return len(self.purchase_history) > 0