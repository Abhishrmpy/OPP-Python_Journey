
import csv

class Item:
    pay_rate = 0.8
    all = [] # class attribute to store all instances of item
    def __init__(self, name:str, price:float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"quantity {quantity} is not greater than or equal to zero!"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Action to excute
        Item.all.append(self)

    #This is the action we want to perform in our class
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_dicount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            item(
                name = item.get(name),
                price = item.get(price),
                quantity = item.get(quantity),
                )

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

Item.instantiate_from_csv()
print(Item.all)
    