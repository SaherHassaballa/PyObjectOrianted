class medical:
    def __init__(self, name, price_per_unit, quantity, expiry_date):
        self.name = name
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        self.expiry_date = expiry_date


    def add_stock(self, quantity):
        self.quantity += quantity
        print(f"Added {quantity} units of {self.name}. New quantity: {self.quantity}")
        return
    def sale(self, quantity):
        if quantity > self.quantity:
            print(
                f"Insufficient stock for {self.name}. Available quantity: {self.quantity}"
            )
            try_again = input("Would you like to try again? (yes/no): ").strip().lower()
            if try_again == "yes":
                new_quantity = int(input("Enter the quantity you want to sell: "))
                self.sale(new_quantity)
            else:
                print("Sale cancelled.")
        self.quantity -= quantity
        print(
            f"Sold {quantity} units of {self.name}. Remaining quantity: {self.quantity}"
        )

    def __str__(self):
        print(
            f"Medical Item: {self.name}, Price per Unit: {self.price_per_unit}, Quantity: {self.quantity}, Expiry Date: {self.expiry_date}"
        )
        return
