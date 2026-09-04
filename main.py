from models import Product, Customer, OrderItem, Order
from store import Store
import datetime

product_1 = Product(1, "Mouse", 10, 500000, "2027-01-01")
product_2 = Product(2, "kyboard", 30, 100000, "2028-01-01")
customer = Customer(1, "Ali", 2000000, "09123456789")
item_1 = OrderItem(product_1, 3)
item_2 = OrderItem(product_2, 2)
order = Order(123, customer , "9/4/20206")
order.add_item(item_1)
order.add_item(item_2)


kazem = Store()
kazem.add_product(product_1)
kazem.add_product(product_2)
kazem.add_customer(customer)
items = [item_2, item_1]
date = datetime.date.today
kazem.create_order(1, items, date)
kazem.complete_order(1)
kazem.show_orders()
print(kazem.balance)





