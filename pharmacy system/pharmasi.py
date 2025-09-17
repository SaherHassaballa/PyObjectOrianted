from math import e
from client import *
from suplier import *
from medical import *
class pharmasi:
    def __init__(self):
        self.suppliers = []
        self.clients = []
        self.medical_objects = []
    
    def supplier(self):
        self.name = input("Enter supplier name:")
        self.contact_info = input("Enter supplier contact info:")
        if [supplier for supplier in self.suppliers if supplier.name.lower() == self.name.lower() ] != []:
            print("Supplier already exists.")
            self.supplier_state = input("Do you want to add items? (yes/no): ").strip().lower()
            if self.supplier_state == 'yes':
                self.suplier_item_name =input("Enter item name: ")
                for omedical in self.medical_objects:
                    if omedical.name.lower() == self.suplier_item_name.lower():
                        print("Item already exists.")
                        num_of_additional_items = int(input("Enter number of additional items: "))
                        omedical.add_stock(num_of_additional_items)
                        self.existing_medical = True
                        break
                    else:
                        self.existing_medical = False
                if self.existing_medical == False:
                    self.suplier_item_price = float(input("Enter item price: "))
                    self.suplier_item_quantity = int(input("Enter item quantity: "))
                    self.suplier_item_expiry_date = input("Enter item expiry date: ")
                    self.new_medical = medical(self.suplier_item_name, self.suplier_item_price, self.suplier_item_quantity, self.suplier_item_expiry_date)
                    self.medical_objects.append(self.new_medical)
        else:
            osupplier = suplier(self.name, self.contact_info)
            self.suppliers.append(osupplier)
            self.suplier_item_name = input("Enter item name: ")
            self.suplier_item_price = float(input("Enter item price: "))
            self.suplier_item_quantity = int(input("Enter item quantity: "))
            self.suplier_item_expiry_date = input("Enter item expiry date: ")
            new_medical = medical(self.suplier_item_name, self.suplier_item_price, self.suplier_item_quantity, self.suplier_item_expiry_date)
            osupplier.add_supplied_item(new_medical)
            self.medical_objects.append(new_medical)

        
    def clinet(self ):
        
        self.name = input("Enter client name: ")
        self.age = int(input("Enter client age: "))
        self.contact_info = input("Enter client contact info: ")
        self.choice = input("add purchase press 1 or cancel press 2 : ").strip().lower()
        if self.choice == '1':
            oclient = client(self.name, self.age, self.contact_info)
            purchase = input("Enter purchase item: ").strip().lower()
            for omedical in self.medical_objects:
                if omedical.name.lower() == purchase:
                    total_price = omedical.price_per_unit * omedical.quantity
                    oclient.add_purchase(omedical, total_price)
                    omedical.sale(omedical.quantity)
                    print(f"Purchase added: {omedical.name}, Total Price: {total_price}")
                    break
            
