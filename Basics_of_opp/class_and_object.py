class laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_detail(self):
        print(f"brand:{self.brand},model:{self.model},price:{self.price}")


# Creating multiple Laptop objects
laptop1 = laptop("Dell", "Inspiron 15", 69999)
laptop2 = laptop("HP", "pavilion", 54321)
laptop3 = laptop("Apple", "macbook pro", 199999)

# Storing objects in a list
laptops = [laptop1, laptop2, laptop3]

#itreating through the list of laptops and displaying their details 
for lap in laptops:
    lap.show_detail()