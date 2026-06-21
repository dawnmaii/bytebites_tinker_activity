# ByteBites — UML Class Document

## Classes

```
+-----------------------------------------------+
|                    Item                       |
+-----------------------------------------------+
| - name             : str                      |
| - price            : float                    |
| - category         : str                      |
| - popularity_rating: float                    |
+-----------------------------------------------+
| + __init__(name, price, category,             |
|            popularity_rating)                 |
+-----------------------------------------------+

+-----------------------------------------------+
|                   Catalog                     |
+-----------------------------------------------+
| - items : list[Item]                          |
+-----------------------------------------------+
| + __init__()                                  |
| + add_item(item: Item)                        |
| + filter_by_category(category: str)           |
|     -> list[Item]                             |
+-----------------------------------------------+

+-----------------------------------------------+
|                  Customer                     |
+-----------------------------------------------+
| - name             : str                      |
| - purchase_history : list[Transaction]        |
+-----------------------------------------------+
| + __init__(name: str)                         |
| + record_purchase(transaction: Transaction)   |
| + is_verified() -> bool                       |
+-----------------------------------------------+

+-----------------------------------------------+
|                 Transaction                   |
+-----------------------------------------------+
| - selected_items : list[Item]                 |
+-----------------------------------------------+
| + __init__()                                  |
| + add_to_order(item: Item)                    |
| + compute_total() -> float                    |
+-----------------------------------------------+
```

---

## Relationships

```
Customer 1 ──────────────── 0..* Transaction
             purchase_history

Transaction 1 ───────────── 1..* Item
               selected_items

Catalog 1 ───────────────── 0..* Item
              items
```

| Relationship | Type | Description |
|---|---|---|
| `Customer` → `Transaction` | Association (has-many) | `purchase_history` holds all of a customer's past transactions |
| `Transaction` → `Item` | Composition (has-many) | `selected_items` groups the items chosen in this order |
| `Catalog` → `Item` | Aggregation (has-many) | `items` holds the full store of available food items |

---

## Naming Rationale

| Old name | Revised name | Class | Reason |
|---|---|---|---|
| `collection` | `Catalog` | — | Clearer domain term; avoids confusion with Python's `collections` module |
| `items` | `selected_items` | `Transaction` | `items` alone is generic; `selected_items` anchors the attribute to its purpose inside a transaction |
| `add_item()` | `add_to_order()` | `Transaction` | Within a transaction the action is building an order, not just appending to a list |
| `add_to_history()` | `record_purchase()` | `Customer` | Describes what is actually happening — a completed purchase is being recorded against the customer |
