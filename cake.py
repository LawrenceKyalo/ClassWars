show_expected_result = True
show_hints = True

class Cake:
    def __init__(self, kind, price, slices):
        """
        Initialize the Cake class with kind, price, and slices.
        :param kind: The type of cake.
        :param price: The price of the cake.
        :param slices: The number of slices in the cake.
        """
        self.kind = kind
        self.price = price
        self.slices = slices

    def describe(self):
        """
        Returns a string describing the cake.
        """
        return f"This is a {self.kind} cake, priced at ${self.price} with {self.slices} slices."
    
spice_cake = Cake("spice", 20, 8)
chocolate_cake = Cake("chocolate", 25, 10)

print(chocolate_cake.describe())
print(spice_cake.describe())