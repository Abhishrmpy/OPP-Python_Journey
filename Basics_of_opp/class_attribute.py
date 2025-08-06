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

    def __repr__(self):
        return f"Item('{self.name}',{self.price}',{self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# for instance in Item.all:
#     print(instance.name)

print(Item.all)
    