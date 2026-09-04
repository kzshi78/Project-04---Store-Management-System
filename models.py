class Product:
    def __init__(self, product_id, name, stock, price, expiration_date):
        self.product_id = product_id
        self.name = name
        self.stock = stock
        self.price = price
        self.expiration_date = expiration_date

    def info(self):
        return(
            f"Product_ID: {self.product_id}\n"
            f"Name: {self.name}\n"
            f"Stock: {self.stock}\n"
            f"Price: {self.price}\n"
            f"Expiration_Date: {self.expiration_date}"
        )

    def __str__(self):
        return self.info()


class Customer:
    def __init__(self, customer_id, name, balance, phone):
        self.customer_id = customer_id
        self.name = name
        self.balance = balance
        self.phone = phone

    def info(self):
        return(
            f"Customer_ID: {self.customer_id}\n"
            f"Name: {self.name}\n"
            f"Balance: {self.balance}\n"
            f"Phone: {self.phone}"
        )
    def __str__(self):
        return self.info()

class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self):
        subtotal = self.product.price * self.quantity
        return subtotal
    
    def __str__(self):
        return (
            f"Product: {self.product.name}\n"
            f"Quantity: {self.quantity}\n"
            f"Subtotal: {self.calculate_subtotal()}"
        )

class Order:
    def __init__(self, order_id, customer, date):
        self.order_id = order_id
        self.customer = customer
        self.items = []
        self.date = date
        self.status = "Pending"
        
    def add_item(self, new_item):
        self.items.append(new_item)

    def remove_item(self, item):
        for it in self.items:
            if it == item:
                self.items.remove(item)
                return
        print("Not Found Item")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.calculate_subtotal() 
        return total

    def show_order(self):    
        order_info = (
            f"Order_ID: {self.order_id}\n"
            f"Customer: {self.customer}\n"
            f"Date: {self.date}\n"
            f"Items:\n"
        )

        for item in self.items:
            order_info += str(item) + "\n"

        order_info += (
            f"Total_Price: {self.calculate_total()}\n"
            f"Status: {self.status}"
        )

        return order_info
    
    def complete_order(self):
        self.status = "Complete"
        

    def cancel_order(self):
      if self.status == "Pending":
        self.status = "Cancelled"
        return True
      
      return False
    def __str__(self):
        return self.show_order() 
    