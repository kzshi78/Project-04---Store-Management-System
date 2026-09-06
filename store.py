from models import Product,Customer,OrderItem,Order
import datetime

class Store:
    def __init__(self):
        self.products = []
        self.customers = []
        self.orders = []
        self.order_counter = 1
        self.balance = 0

    def add_product(self, new_product):
        self.products.append(new_product)
        
    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return
        print("Not Found Product")

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        print("Not Found Product")

    def show_products(self):
        for product in self.products:
                print(product)
        
    def get_available_products(self):
        return list(
            filter(lambda product: product.stock > 0, self.products)
        )   

    def show_available_products(self):

        products = self.get_available_products()

        for product in products:
            print(product)


    def get_product_names(self):
        return list(
            map(lambda product: product.name, self.products)
        )

    def get_expensive_products(self, price):
        return list(
            filter(lambda product: product.price > price, self.products)
        )
    
    def add_customer(self, new_customer):
        self.customers.append(new_customer)

    def search_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        print("Not Found Customer")

    def create_order(self, customer_id, items):
        if not isinstance(items, list):
            raise TypeError("Items must be a list.")
        
        customer = None
        for c in self.customers:
            if c.customer_id == customer_id:
                customer = c
                break

        if customer == None:
            print("Customer Not Found")
            return

        for item in items:
                
            if not isinstance(item, OrderItem):
                raise TypeError("Each item must be an OrderItem.")
            if item.quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")
            if item.product.stock < item.quantity:
                print("Not Enough Stock")
                return
        
        order_id = self.order_counter
        self.order_counter += 1
        date = datetime.date.today()
        order = Order(order_id, customer, date)
        for item in items:
            order.add_item(item)

        total = order.calculate_total()

        if customer.balance < total:
            print("Not Enough Balance")
            return
        self.orders.append(order)
       
        

    def complete_order(self, order_id):
        order = None

        for o in self.orders:
            if o.order_id == order_id:
                order = o
                break

        if order == None:
            print("Order Not Found")
            return

        if order.status != "Pending":
            print("Order is not pending")
            return   

        for item in order.items:
            item.product.stock -= item.quantity
        total = order.calculate_total()
        order.customer.balance -= total
        self.balance += total
        order.status = "Completed"
        return
        
        
    def cancel_order(self, order_id):

        order = None

        for o in self.orders:
            if o.order_id == order_id:
                order = o
                break

        if order == None:
            print("Order Not Found")
            return

        if order.status != "Pending":
            print("Cannot Cancel Order")
            return
        order.status = "Cancelled"

    def search_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order

        print("Order Not Found")     

    def show_orders(self):
        for order in self.orders:
            print(order)
            

            
        