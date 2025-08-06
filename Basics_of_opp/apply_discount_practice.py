#for appplying dicount we use class attributes and methods
#class attributes are shared by all instances of the class 

class Item:
    pay_rate = 0.8 #clas attrubute for discount rate
    def __init__(self, name:str, price:float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"quantity {quantity} is not greater than or equal to zero!"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("laptop", 500, 5)
item1.apply_discount()
print(item1.price)

item3 = Item("phone", 400, 4)
item3.pay_rate = 0.6
item3.apply_discount()
print(item3.price)

item2 = Item("phone", 400, 4)
item2.pay_rate = 0.7  # instance-level override
item2.apply_discount()
print(item2.price)  # Output: 280.0 ✅







    