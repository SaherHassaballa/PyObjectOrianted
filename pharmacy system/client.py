class client:
    def __init__ (self, name, age, contact_info):
        self.name = name
        self.age = age
        self.contact_info = contact_info
        self.purchases = []
        self.total_prices = 0

    def add_purchase(self, purchase , total_price):
        self.purchases.append(purchase)
        self.total_prices += total_price
    
    def __str__(self) :
        print(f"Client Name: {self.name}, Age: {self.age}, Contact Info: {self.contact_info}, Purchases: {len(self.purchases) , self.total_prices}")
        return