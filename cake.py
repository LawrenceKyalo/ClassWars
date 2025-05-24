# cake.py
# This code defines a class structure for a cake shop, including an Item class and a Cake class.
# The Item class represents a generic item with a type and price.
# The Cake class inherits from Item and adds specific attributes and methods for cakes.
class Item:
    def __init__(self, item_type, price):
        self.item_type = item_type
        self._price = price

    @property
    def price(self):
        """
        Returns the price of the item.
        """
        return self._price
    
           
class Cake(Item):
    def __init__(self, flavor, price, slices):
        """
        Initialize the Cake class with kind, price, and slices.
        :param kind: The type of cake.
        :param price: The price of the cake.
        :param slices: The number of slices in the cake.
        """
        super().__init__("cake", price)
        self.flavor = flavor
        self._price = price
        self.slices = slices
        #self.sold_slices = 0
        self.remaining_slices = slices

    def describe(self):
        """
        Returns a string describing the cake.
        """
        return f"This is a {self.flavor} cake, priced at ${self.price} with {self.slices} slices."
    
    def sell(self, count):
        """
        Sells a specified number of slices of the cake.
        :param count: The number of slices to sell.
        :return: The number of remaining slices.
        """
        if count <= 0:
            return (f"Invalid number of slices. Please enter a positive number.")
        elif count > self.remaining_slices:
            return (f"Not enough slices left. Only {self.remaining_slices} slices available.")            
        else:
            self.remaining_slices -= count
            return (f"{count} slices sold. {self.remaining_slices} slices remaining.")
        
    def __eq__(self, other):
        return self.remaining_slices*(self.price/self.slices) == other.remaining_slices*(other.price/other.slices)

    def __lt__(self, other):
        return self.remaining_slices*(self.price/self.slices) < other.remaining_slices*(other.price/other.slices)
    
    def __gt__(self, other):
        return self.remaining_slices*(self.price/self.slices) > other.remaining_slices*(other.price/other.slices)
    
spice_cake = Cake("spice", 18, 8)
chocolate_cake = Cake("chocolate", 24, 6)

print(spice_cake.sell(5))
print(spice_cake.sell(4))

print(chocolate_cake.sell(-1))
print(chocolate_cake.sell(0))

