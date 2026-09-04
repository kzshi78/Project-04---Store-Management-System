from models import Product, Customer, OrderItem, Order

product_1 = Product(1, "Mouse", 10, 500000, "2027-01-01")
product_2 = Product(2, "kyboard", 30, 10000, "2028-01-01")
customer = Customer(1, "Ali", 2000000, "09123456789")
item_1 = OrderItem(product_1, 3)
item_2 = OrderItem(product_2, 5)
order = Order(123, customer , "9/4/20206")
order.add_item(item_1)
order.add_item(item_2)
print(order)






