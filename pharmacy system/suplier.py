class suplier:
    def __init__(self , name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.supplied_items = []

    def add_supplied_item(self, item):
        self.supplied_items.append(item)
        print(f"Item {item.name} added to supplier {self.name}'s supplied items.")
        return
    
    def __str__(self):
        print(f"Supplier Name: {self.name}, Contact Info: {self.contact_info}, Supplied Items: {len(self.supplied_items)}")
        return