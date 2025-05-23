show_expected_result = True
show_hints = True

class Cake:
    def __init__(self, flavor, price, slices):
        """
        Initialize the Cake class with kind, price, and slices.
        :param kind: The type of cake.
        :param price: The price of the cake.
        :param slices: The number of slices in the cake.
        """
        self.flavor = flavor
        self.price = price
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
        if count > self.remaining_slices:
            print(f"Not enough slices left. Only {self.remaining_slices} slices available.")
            return self.remaining_slices
        else:
            self.remaining_slices -= count
            return self.remaining_slices
    
spice_cake = Cake("spice", 18, 8)
chocolate_cake = Cake("chocolate", 24, 6)

print(spice_cake.sell(5))
print(spice_cake.sell(4))

print(chocolate_cake.sell(-1))
print(chocolate_cake.sell(0))

