from models import Product, Customer, OrderItem, Order
from store import Store
import datetime

store = Store()

product1 = Product(
    1,
    "Mouse",
    10,
    500000,
    "2027-01-01"
)

product2 = Product(
    2,
    "Keyboard",
    5,
    1000000,
    "2027-02-01"
)

product3 = Product(
    3,
    "Monitor",
    3,
    5000000,
    "2028-01-01"
)

store.add_product(product1)
store.add_product(product2)
store.add_product(product3)


customer1 = Customer(
    1,
    "Ali",
    10000000,
    "09123456789"
)

customer2 = Customer(
    2,
    "Reza",
    20000000,
    "09987654321"
)

store.add_customer(customer1)
store.add_customer(customer2)



item1 = OrderItem(product1, 2)

item2 = OrderItem(product2, 1)

order = Order(
    1,
    customer1,
    "2026-09-05"
)

order.add_item(item1)
order.add_item(item2)

store.orders.append(order)


items = [
    OrderItem(product1, 1),
    "Keyboard"
]

try:
    store.create_order(1, items)

except TypeError as error:
    print(error)
