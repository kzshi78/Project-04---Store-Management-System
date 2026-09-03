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
            f"Product: {self.product}"
            f"Quantity: {self.quantity}"
            f"Subtotal: {self.calculate_subtotal}"
        )

class Order():
    def __init__(self):
        pass
