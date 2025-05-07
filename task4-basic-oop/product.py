"""
definition of the product class for managing inventory in invetory system

 """

class Product:
    """
    THIS IS ACLASS FOR REPRESENTING A PRODUCT IN INVESTORY .
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        THIS IS INITIALISING A PRODUCT OBJECT WITH NAME ,PRICE AND QUANTITY
        """
       
        self._name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self) -> str:
        """outputs the name of the product."""
        return self._name

    @property
    def price(self) -> float:
        """gets the price of the product."""
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price must not be negative.")
        self._price = value

    @property
    def quantity(self) -> int:
        """Gets the quantity in stock."""
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value

    def add_inventory(self, amount: int):
        """
        addition of the invetory quantity.

        """
        if amount <= 0:
            raise ValueError("Amount to add must be positive.")
        self.quantity += amount

    def remove_inventory(self, amount: int):
        """
        removes fromm the investory quantity.

        """
        if amount <= 0:
            raise ValueError("Amount to remove must be positive.")
        if amount > self.quantity:
            raise ValueError("Not enough inventory to remove that amount.")
        self.quantity -= amount

    def total_value(self) -> float:
        """
        Calculates total value of product in stock.
       
        """
        return self.price * self.quantity

    def display_info(self) -> str:
        """
        Returns a changed string of product details. 
        """
        return (
            f"product :{self.name}"
            f"Price: ${self.price:.2f}, "
            f"Quantity: {self.quantity}, "
            f"Total Value: ${self.total_value():.2f}"
        )
