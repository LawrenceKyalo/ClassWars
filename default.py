class MyClass:
    """
    A simple Python class example.
    """
    #constructor function
    def __init__(self, attribute):
        """
        Initialize the class with an attribute.
        :param attribute: Any value to initialize the class attribute.
        """
        self.attribute = attribute
        #private attribute
        self._private_attribute = "This is a private attribute"

    def get_attribute(self):
        """
        Returns the value of the attribute.
        """
        return self.attribute

    def set_attribute(self, value):
        """
        Sets the value of the attribute.
        :param value: The new value for the attribute.
        """
        self.attribute = value

    def __eq__(self, value):
        pass

    def __lt__(self, value):
        pass

    def __gt__(self, value):
        pass

    print("Test")
        
        